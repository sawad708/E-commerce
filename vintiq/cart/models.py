from django.db import models
from accounts.models import UserProfile
from product.models import Product, Coupon


# Create your models here.

class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=True)
    
    def get_total_price(self):
        total_price = sum(item.get_total_price() for item in self.cart_items.all())
        return total_price
    
    
class Cart_item(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def get_total_price(self):
        if self.product is not None:
            return self.product.price * self.quantity
        