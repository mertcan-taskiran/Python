from django.contrib import admin
from django.urls import path
from . import views # Şuan ki klasördeki views

app_name="user"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),

]