from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

# def detail(request, id): # Dinamik URL
#     return HttpResponse("Detail:" + str(id))

def dashboard(request):

    products = Product.objects.filter(seller = request.user)
    
    context = {
        "products":products
    }

    return render(request, "dashboard.html", context)

def addProduct(request):

    form = ProductForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        product = form.save(commit=False) # Kaydetme, sadece obje oluştur.
        product.seller = request.user
        product.save()
        messages.success(request,"Başarıyla ürün eklendi.")
        return redirect("index")

    return render(request, "addproduct.html", {"form":form})

def detail(request, id):
    # product = Product.objects.filter(id=id).first()
    product = get_object_or_404(Product, id=id)
    return render(request, "detail.html", {"product": product})
