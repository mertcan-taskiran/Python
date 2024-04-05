# Generated by Django 4.2.11 on 2024-04-05 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_product_product_image_alter_product_content_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="price",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=10, verbose_name="Fiyat"
            ),
            preserve_default=False,
        ),
    ]