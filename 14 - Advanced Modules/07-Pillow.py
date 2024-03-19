from PIL import Image,ImageFilter

image = Image.open("images/kus.jpg")

# image.show() # Resmi gösterir.

# image.save("images/kus2.jpg") # Aynı resmi kaydeder.

# image.rotate(180).save("images/kus3.jpg") # 180 derece döndürür.

# image.convert(mode = "L").save("images/kus4.jpg") # Resmi siyah beyaz yapar.

# degistir = (100,100)
# image.thumbnail(degistir)
# image.save("images/kus5.jpg") # Resim boyutunu değiştirir.

# image.filter(ImageFilter.GaussianBlur(10)).save("images/kus6.jpg") # Blur