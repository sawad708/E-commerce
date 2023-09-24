from django.shortcuts import render,redirect
from .models import Category
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def list_categories(request):
    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request, 'category/category_list.html', context)


@login_required(login_url='login') 
def add_category(request):
    if request.method == 'POST':
        slug = request.POST['slug']
        category_name = request.POST['name']
        category_description = request.POST['description']
        category_image = request.FILES.get('image')
        
        check = [slug, category_name, category_description]
        for values in check:
            if values == '':
                messages.info(request, 'Some feilds are empty')
                return redirect(add_category)
            else:
                pass
            
        if Category.objects.filter(category_name=category_name).exists():
            messages.info(request, 'category name already exist')
            return redirect(add_category)
        elif Category.objects.filter(slug=slug).exists():
            messages.info(request, 'slug already exist')
            return redirect(add_category)
        else:
            categories = Category.objects.create(
            slug = slug,
            category_name = category_name,
            category_description = category_description,
            category_image = category_image,
            is_available = True
            )   
            categories.save()
        return redirect(list_categories)
    else:
        pass
    return render(request,'category/add_category.html')


@login_required(login_url='login')
def edit_category(request, id):
    if request.method == 'POST':
        slug = request.POST['slug']
        category_name = request.POST['name']
        category_description = request.POST['description']
        category_image = request.FILES.get('image', None)
        
        category = Category.objects.filter(id=id).first()
        
        if category:
            category.slug = slug
            category.category_name = category_name
            category.category_description =category_description
            
            if category_image is not None:
                category.category_image = category_image
                
            category.save()
            
        return redirect('category')
                

# def delete_category(request,id):
#     category = Category.objects.get(id=id)
#     category.delete()
#     return redirect(list_categories)


@login_required(login_url='login')
def block_category(request, id):
    category = Category.objects.get(id=id)
    if category.is_available == True:
        category.is_available = False
    else:
        category.is_available = True
    category.save()
    return redirect('category')