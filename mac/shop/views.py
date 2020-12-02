from django.shortcuts import render
from .models import Product
from math import ceil

from django.http import HttpResponse

# Create your views here.
def index(request):
  products = Product.objects.all()
  print(products)
  n = len(products)
  nSlides = n//4 + ceil((n/4)-(n//4))
  params = {'no_of_slides': nSlides, 'range':range(1, nSlides), 'product': products}
  return render(request, 'shop/index.html', params)

def about(request):
  return render(request, 'shop/about.html') 

def contact(request):
  return render(request, 'shop/contact.html')

def tracker(request):
  return HttpResponse("WE ARE AT TRACKER")    

def search(request):
  return HttpResponse("WE ARE AT Search")

def prodView(request):
  return HttpResponse("WE ARE AT Product View") 

def checkout(request):
  return HttpResponse("WE ARE AT CHECKOUT")     