from decimal import Decimal

from store.models import Product


class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('sesskey')
        if 'sesskey' not in request.session:
            cart = self.session['sesskey'] = {}
        self.cart = cart    
        
    def add(self, product, product_qty):
        product_id = product.id
        
        ## Grabbing data from the carted product and saving into session
        if product_id not in self.cart:
            self.cart[product_id] = {'price': str(product.price), 'quantity': int(product_qty)}
        
        self.session.modified = True
        
    def __len__(self):
        """
        Get the number of items in the cart
        """
        return sum(item['quantity'] for item in self.cart.values())
    
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.products.filter(id__in=product_ids)
        cart = self.cart.copy()
        
        for product in products:
            cart[str(product.id)]['product'] = product
            
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
            
    def get_total_cart_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
