from django.db import models
from brand.models import Brand
from category.models import Category

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to="photos/categories")
    is_availiable = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    def is_outofstock(self):
        return self.stock <= 0
    
    
    
    def __str__(self):
        return self.product_name
    
    
class productImage(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_image")
    pr_images = models.ImageField(upload_to="photos/products")
    
    def __str__(self):
        return self.Product.product_name + 'image'
    
    
    
class Coupon(models.Model):
    Coupon_code = models.CharField(max_length=10)
    is_expired = models.BooleanField(default=False)
    end_date = models.DateField(null=True)
    discount_price = models.IntegerField(default=100)
    minimum_amount = models.IntegerField(default=500)