from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.adminpannel, name="admin_pannel"),
    path('coupon_list/', views.coupon_list, name="coupon_list"),
    path('add_coupon/', views.add_coupon, name="add_coupon"),
    # path('category/', views.category, name="category"),
    path('admin_user/', include('admin_user.urls')),
    path('category/', include('category.urls')),
    path('brand/', include('brand.urls')),
    path('product/', include('product.urls')),
    path('order_views/<int:id>', views.order_views, name="order_views"),
    
    
]