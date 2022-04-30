from decimal import Decimal

from store.models import Product


class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('sesskey')
        if 'sesskey' not in request.session:
            cart = self.session['sesskey'] = {}
        self.cart = cart    
        
    def save(self):
        self.session.modified = True
        
    def add(self, product, product_qty):
        product_id = str(product.id)
        
        # Grabbing data from the added product and saving into session
        if product_id not in self.cart:
            self.cart[product_id] = {'price': str(product.price), 'quantity': int(product_qty)}
        else:
            self.cart[product_id]['quantity'] = product_qty
        
        self.save()
    
    def delete(self, product):
        """
        Delete item from user session data
        """
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]
        
        self.save()
        
    def update(self, product, quantity):
        """
        Update values in session data
        """
        product_id = str(product)
        product_quantity = quantity
        
        if product_id in self.cart:
            self.cart[product_id]['quantity'] = product_quantity
            
        self.save()
        
    def __len__(self):
        """
        Get the quantity number for items in the cart
        """
        return sum(item['quantity'] for item in self.cart.values())
    
    def __iter__(self):
        """
        Iterate through items in the session data, add product data to db, 
        and return products with total_price field
        """
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
