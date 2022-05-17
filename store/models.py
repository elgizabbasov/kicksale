""" Elgiz Abbasov
    Tables
"""
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.core.validators import MinValueValidator
from decimal import Decimal


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(in_stock=True)


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name
    
    def get_abs_url(self):
        return reverse('store:categories_list', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='product_created_by', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    ## TODO: Multiple images - Only one image per product possible currently
    image = models.ImageField(upload_to='images/', default='images/default.png')
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
    product = models.ForeignKey(Product, related_name='sizes', on_delete=models.CASCADE)
    in_stock = models.BooleanField(default=True)
    prod_size = models.DecimalField(max_digits=3, decimal_places=1)
    created = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.prod_size)
        
    class Meta:
        verbose_name_plural = 'Sizes'
        ordering = ('-created',)
        # TODO: #4
        unique_together = ( 
                           ("product", "prod_size"),
        )
