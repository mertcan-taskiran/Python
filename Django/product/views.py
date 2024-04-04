from django.shortcuts import render, HttpResponse, redirect
from .forms import ProductForm
from django.contrib import messages
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

    form = ProductForm(request.POST or None)

    if form.is_valid():
        product = form.save(commit=False) # Kaydetme, sadece obje oluştur.
        product.seller = request.user
        product.save()
        messages.success(request,"Başarıyla ürün eklendi.")
        return redirect("index")

    return render(request, "addproduct.html", {"form":form})