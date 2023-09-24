from django.shortcuts import render,redirect
from product.models import Product,productImage
from brand.models import Brand
from category.models import Category

# Create your views here.
def shop(request):
    products = Product.objects.all().filter(is_availiable = True)
    category_id = request.GET.get('category')
    brand_id = request.GET.get('brand')
    
    if category_id:
        products = products.filter(category__id=category_id, is_availiable=True)
        
    if brand_id:
        products = products.filter(brand__id=brand_id, is_availiable=True)
        
    # if request.method == 'POST':
    #     searched = request.POST['searched']
    #     products = Product.objects.filter(product_name = searched)
    #     return render(request, 'shop/shop.html', {'products':products})
        
        
    brands = Brand.objects.filter(is_availiable=True)
    categories = Category.objects.filter(is_available=True)
    context = {
        'products':products,
        'categories':categories,
        'brands':brands
        }
    
    
    
    return render(request, 'shop/shop.html', context)

def product_detailes(request, id):
    products = Product.objects.filter(id=id)
    context = {
        'products':products
    }
    return render(request, 'shop/product_detailes.html', context)