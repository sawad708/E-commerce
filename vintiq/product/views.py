from django.shortcuts import render, redirect
from .models import Product,productImage
from django.contrib import messages
from brand.models import Brand
from category.models import Category
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def products(request):
    products = Product.objects.all()
    brands = Brand.objects.all()
    context = {
        'products' : products,
        'brands':brands,
        
         
    }
    return render(request, 'product/product_list.html', context)


def add_product(request):
    brands=Brand.objects.filter(is_availiable=True)
    context= {'brands':brands}
    if request.method == "POST":
        image = ''
        try:
            image = request.FILES['image']
        except:
            if image == '':
                messages.info(request, "image feild can't be empty")
                return redirect(add_product)
            
        name = request.POST['name']
        brand = request.POST['brand']
        category = request.POST['category']
        description = request.POST['description']
        price = request.POST['price']
        stock = request.POST['stock']
        images = request.FILES.getlist('images')
        

        brand_instance = Brand.objects.get(brand_name=brand, is_availiable=True)
        category_instance = Category.objects.get(id=category, is_available=True)
            
        product=Product.objects.create(
                product_name = name,
                brand = brand_instance,
                category = category_instance,
                description = description,
                price = price,
                stock = stock,
                image = image,
                
                
                
        )
        product.save()
        product = Product.objects.get(product_name=name)
        for image in images:
            productImage.objects.create(Product=product, pr_images=image)
            
        return redirect(products)
    return render(request, 'product/product.html', context)
        
        
def edit_product(request, id):

    if request.method == "POST":
        name = request.POST['name']
        brand = request.POST['brand']
        category = request.POST['category']
        description = request.POST['description']
        price = request.POST['price']
        stock = request.POST['stock']
        
        brand_instance =Brand.objects.get(brand_name=brand, is_availiable=True)
        
        category_instance = Category.objects.get(id=category, is_availiable=True)
        
        product = Product.objects.filter(id=id).first()
        
        if product:
            product.product_name = name
            product.brand = brand_instance
            product.category = category_instance
            product.description = description
            product.price = price
            product.stock = stock
            
            product.save()
            
        return redirect('product')
    

    
# def delete_product(request, id):
#     product = Product.objects.get(id=id)
#     product.delete()
#     return redirect('product')

def block_product(request, id):
    product = Product.objects.get(id=id)
    if product.is_availiable == True:
        product.is_availiable = False
    else:
        product.is_availiable = True
    product.save()
    return redirect('product')


