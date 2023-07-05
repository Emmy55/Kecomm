
from . models import Category, Product 
from django.shortcuts import render

from cart.forms import CartAddProductForm

from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required


import re
from bs4 import BeautifulSoup
from django.db.models import Q


def home(request,category_slug=None):
    category = None
    categories = Category.objects.all()

    products = Product.objects.filter(available=True)
    # new_price = Product.formatted_price
    if category_slug:
        category = get_object_or_404(Category,
                                     slug=category_slug)
        products = products.filter(category=category)
    
    context = {
        'category' : category,
        'categories': categories,
        'products': products,
        # 'new_price': new_price,
        }
    
    if request.resolver_match.url_name == 'home':
        template_name = 'kobosh/home.html'
    else:
        template_name = 'kobosh/categories.html'
    return render(request, template_name, context)


def product_detail(request, id, slug,category_slug=None):
    category = None
    categories = Category.objects.all()

    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category,
                                     slug=category_slug)
        products = products.filter(category=category)
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()

    products = Product.objects.filter(available=True)


    context = {
        'product' : product,
        'products': products,
        'cart_product_form': cart_product_form,
        'category' : category,
        'categories': categories,
        }
    
    

    return render(request, 'kobosh/details.html', context)


def payment(request,category_slug=None):
    category = None
    categories = Category.objects.all()

    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category,
                                     slug=category_slug)
        products = products.filter(category=category)
    
    context = {
        'category' : category,
        'categories': categories,
        'products': products
        }
    
    return render(request, 'kobosh/payments.html', context)



def search(request,category_slug=None):
    category = None
    categories = Category.objects.all()

    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category,
                                     slug=category_slug)
        products = products.filter(category=category)
    
  
    if request.method == 'GET':
        query = request.GET.get('query')

        # Search the database for products matching the query
        result = Product.objects.filter(Q(name__icontains=query) | Q(new_price__icontains=query))
        print(result)
        context = {
        'category' : category,
        'categories': categories,
        'results': result,
        }
        return render(request, 'kobosh/result.html',context)
