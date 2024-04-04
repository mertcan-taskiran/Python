from django.db import models

# Create your models here.

class Product(models.Model):
    seller = models.ForeignKey("auth.User", on_delete = models.CASCADE, verbose_name = "Satıcı") # User silindiğinde ona ait olanlarda silinir.
    title = models.CharField(max_length = 50, verbose_name = "Ürün Adı")
    # price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Fiyat")
    content = models.TextField(verbose_name = "İçerik")
    created_date = models.DateTimeField(auto_now_add = True, verbose_name = "Oluşturulma Tarihi") # Eklenme Tarihi

    def __str__(self):
        return self.title # Object yerine 'Title' bilgisini göster.