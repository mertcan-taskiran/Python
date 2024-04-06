from django.contrib import admin
from django.urls import path

from . import views # Şuan ki klasördeki views

app_name = "product"

from product import views

# Url adreslerini parçalıyoruz
urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("addproduct/", views.addProduct, name="addproduct"),
    path("product/<int:id>", views.detail, name="detail"),
    path("update/<int:id>", views.updateProduct, name="update"),
    path("delete/<int:id>", views.deleteProduct, name="delete"),
    path("", views.products, name="products"),
]