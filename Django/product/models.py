from django.db import models

# Create your models here.

class Product(models.Model):
    seller = models.ForeignKey("auth.User", on_delete = models.CASCADE, verbose_name = "Satıcı") # User silindiğinde ona ait olanlarda silinir.
    title = models.CharField(max_length = 50, verbose_name = "Ürün Adı")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Fiyat")
    content = models.TextField(verbose_name = "İçerik")
    created_date = models.DateTimeField(auto_now_add = True, verbose_name = "Oluşturulma Tarihi") # Eklenme Tarihi
    product_image = models.FileField(blank=True, null=True, verbose_name = "Fotoğraf")
    def __str__(self):
        return self.title # Object yerine 'Title' bilgisini göster.
    
class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product", related_name="comments")
    comment_author = models.CharField(max_length=50,verbose_name="İsim")
    comment_content = models.CharField(max_length=200,verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.comment_content