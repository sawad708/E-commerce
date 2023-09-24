from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from product.models import Coupon
from orders.models import Order

# Create your views here.
@login_required(login_url='login')
def adminpannel(request):
    return render(request, 'admin_pannel/index.html')

@login_required(login_url='login')
def coupon_list(request):
    coupon = Coupon.objects.all()
    context = {
        'coupon':coupon,
    }
    return render(request, 'admin_order/coupon_list.html', context)

@login_required(login_url='login')
def add_coupon(request):
    if request.method == 'POST':
        Coupon_code = request.POST['Coupon_code']
        minimum_amount = request.POST['minimum_amount']
        discount_price = request.POST['discount_price']
        expiry_date = request.POST['end_date']
        
        coupon = Coupon.objects.create(
            Coupon_code = Coupon_code,
            minimum_amount = minimum_amount,
            discount_price = discount_price,
            end_date = expiry_date
        )
        coupon.save()
        return redirect(coupon_list)
    return render(request, 'admin_order/add_coupon.html')
    

# def category(request):
#     return render(request, 'admin_user/user_list.html')

@login_required(login_url='login')
def order_views(request, id):
    orders = Order.objects.get(id=id)
    print('==========', orders)
    context = {
       'orders':orders, 
    }
   
    return render(request, 'admin_order/admin_order_view.html', context)