from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def products(request):
    products = Product.objects.all()

    return render(request, "products.html", {"products": products})

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

# def detail(request, id): # Dinamik URL
#     return HttpResponse("Detail:" + str(id))

@login_required(login_url="user:login")
def dashboard(request):

    products = Product.objects.filter(seller = request.user)
    
    context = {
        "products":products
    }

    return render(request, "dashboard.html", context)

@login_required(login_url="user:login")
def addProduct(request):

    form = ProductForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        product = form.save(commit=False) # Kaydetme, sadece obje oluştur.
        product.seller = request.user
        product.save()
        messages.success(request,"Ürün başarıyla eklendi.")
        return redirect("product:dashboard")

    return render(request, "addproduct.html", {"form":form})

def detail(request, id):
    # product = Product.objects.filter(id=id).first()
    product = get_object_or_404(Product, id=id)
    return render(request, "detail.html", {"product": product})

@login_required(login_url="user:login")
def updateProduct(request, id):
    product = get_object_or_404(Product, id=id)
    # instance ile ilk değerler güncellenmemiş haliyle gelir. Daha sonra post yaptığımızda article form tekrar yenilenecek.
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        product = form.save(commit=False)
        product.seller = request.user
        product.save()
        messages.success(request,"Ürün başarıyla güncellendi.")
        return redirect("product:dashboard")

    return render(request, "update.html", {"form":form})

@login_required(login_url="user:login")
def deleteProduct(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    messages.success(request,"Ürün başarıyla silindi.")
    return redirect("product:dashboard")