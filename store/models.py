""" Kicksale store models    
"""
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from decimal import Decimal

from mptt.models import MPTTModel, TreeForeignKey


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(in_stock=True)


class Category(MPTTModel):
    """Category implemented using MPTT
    """
    name = models.CharField(verbose_name=_("Category Name"), 
                            help_text=_("Required and unique"),
                            max_length=255, 
                            unique=True,
                            db_index=True)
    slug = models.SlugField(verbose_name=_("Category URL"),
                            max_length=255, 
                            unique=True)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    is_active = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ["name"]
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        
    def __str__(self):
        return self.name
    
    def get_abs_url(self):
        return reverse('store:categories_list', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.RESTRICT)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='product_created_by', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    ## TODO: Multiple images - Only one image per product possible currently
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    slug = models.SlugField(max_length=255)
    in_stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)
    
    def __str__(self):
        return self.title
    
    def get_abs_url(self):
        return reverse('store:product_info', args=[self.slug])


class Size(models.Model):
    product = models.ForeignKey(Product, related_name='sizes', on_delete=models.RESTRICT)
    in_stock = models.BooleanField(default=True)
    prod_size = models.DecimalField(max_digits=3, decimal_places=1)
    created = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)

    def __str__(self) -> str:
        return str(self.prod_size)
        
    class Meta:
        verbose_name_plural = 'Sizes'
        ordering = ('-created',)
        # TODO: #4
        unique_together = ( 
                           ("product", "prod_size"),
        )

class ProductImage(models.Model):
    """Product images table
    """
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image')
    image = models.ImageField(
        verbose_name=_("Image"),
        help_text=_("Upload a product image"),
        upload_to="images/",
        default="images/default.png",
    )
    is_feature = models.BooleanField(default=False)