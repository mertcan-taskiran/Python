from django.contrib import admin

from .models import Product # Kayıt işlemi

# Register your models here.

# admin.site.register(Product) # Kayıt işlemi

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    search_fields = ["title"] # Sadece title göre arama.

    list_display = ["title", "seller", "created_date"] # Paneldeki tablo görünümü.

    # list_display_links = ["title", "created_date"] # created_date kısmına link gelir.

    # list_filter = ["created_date"] # Filtre görünümü.

    class Meta:
        model = Product
