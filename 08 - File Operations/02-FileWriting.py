try:
    # Dosyayı yazma modunda açma
    with open("yeni_dosya.txt", "w") as dosya:
        # Dosyaya metin yazma
        dosya.write("Bu dosyaya yazılan metin.")

except:
    print("Bir hata oluştu.")