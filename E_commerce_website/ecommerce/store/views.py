from django.shortcuts import render
from .models import * 
from django.contrib.auth.models import User
from django.contrib import messages


def store(request):
    products = Product.objects.all()  # Query all products from the database
    context = {
        'products': products
        }
    return render(request, 'store.html',context)
    

def cart(request):
    
    context = {

    }
    return render(request, 'cart.html', context)


def checkout(request):
    return render(request,'checkout.html')


def home(request):
    featured_products = FeaturedProduct.objects.all()
    return render(request, 'home.html', {'featured_products': featured_products})

