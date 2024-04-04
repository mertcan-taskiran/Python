from django.shortcuts import render, HttpResponse
from .forms import ProductForm

# Create your views here.

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

# def detail(request, id): # Dinamik URL
#     return HttpResponse("Detail:" + str(id))

def dashboard(request):
    return render(request, "dashboard.html")

def addProduct(request):
    form = ProductForm()
    return render(request, "addproduct.html", {"form":form})