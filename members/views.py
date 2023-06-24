from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from kobosh.models import Category, Product 
from django.shortcuts import render, get_object_or_404

def login_user(request,category_slug=None):
    category = None
    categories = Category.objects.all()

    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category,
                                     slug=category_slug)
        products = products.filter(category=category)
    
    
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)

 

            return redirect('kobosh:home')
        else:
            messages.error(request, "There was an error logging in. Please try again.")
            return redirect('members:login_user')

    context = {
        'category' : category,
        'categories': categories,
        'products': products
        }
    
   
    return render(request, 'members/login.html', context)


def signup_user(request,category_slug=None):
    category = None
    categories = Category.objects.all()

    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category,
                                     slug=category_slug)
        products = products.filter(category=category)
    
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("pass")
        password1 = request.POST.get("cpass")
        username = request.POST.get("full_name")

        # Check if passwords match
        if password != password1:
            messages.error(request, "Passwords do not match. Please try again.")
            return redirect('members:signup_user')

        # Validate password
        try:
            validate_password(password)
        except Exception as e:
            messages.error(request, str(e))
            return redirect('members:signup_user')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists. Please use a different email.")
            return redirect('members:signup_user')

        # Create the user
        user = User.objects.create_user(email=email, password=password, username=username)
        user.save()

        return redirect('kobosh:home')

    
    context = {
        'category' : category,
        'categories': categories,
        'products': products
        }


    return render(request, 'members/signup.html', context)

def forgotpass(request,category_slug=None):
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
    return render(request, 'members/forgotpass.html', context)