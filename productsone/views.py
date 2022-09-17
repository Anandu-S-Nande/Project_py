from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
import os
from PIL import Image


# Create your views here.

def home(request):
    products = Product.objects.all()
    data = {
        "products" : products,
    }
    return render(request, 'home.html', data)

def about(request):
  
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST or None, request.FILES or None)
      
        if form.is_valid(): 
            form.save()
            return redirect(page)
        else: 
            return redirect(about) #find two things here how to go the data to admin pannel and then how to set the date to second page

    form = ProductForm()
    data = {
       
        "form" : form
    }
    return render(request, 'page1.html', data)


def page(request):
    products = Product.objects.all()
    # items = os.listdir()
    # for i in item in items:
    #     image1 = Image.open()
    #     im1 = image1.convert('RBG')
    #     print(item)
    #     print(item.split('.')[0])
    #     im1.save()
    data = {
        "products" : products,
    }

    return render(request, 'page.html', data)


