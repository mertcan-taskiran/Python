from django.contrib import admin
from django.urls import path

from . import views # Şuan ki klasördeki views

app_name = "product"

from product import views

# Url adreslerini parçalıyoruz
urlpatterns = [
    path("create/", views.index, name="index"),

]