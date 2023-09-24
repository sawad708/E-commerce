from django.contrib import admin
from .models import Product,productImage,Coupon

# Register your models here.
admin.site.register(Product)
admin.site.register(productImage)
admin.site.register(Coupon)