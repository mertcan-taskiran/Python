try:
    # Dosyayı ekleme modunda açma
    with open("dosya.txt", "a") as dosya:
        # Dosyaya metin ekleme
        dosya.write("\nBu metin dosyaya eklendi.")

except:
    print("Bir hata oluştu.")