from django.shortcuts import render, redirect, get_object_or_404
from kobosh.models import Category, Product
from .cart import Cart
from .forms import CartAddProductForm
from django.contrib.auth.models import User

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if User is None:
        return redirect("members:login")
    else:
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
            
    return redirect('cart:cart_detail')   

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request,category_slug=None):
    category = None
    categories = Category.objects.all()

    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category,
                                     slug=category_slug)
        products = products.filter(category=category)
    
    cart = Cart(request)


    context = {
      'cart': cart,
      'category' : category,
      'categories': categories,
      'products': products
      }
    return render(request, 'cart/cart.html', context)




