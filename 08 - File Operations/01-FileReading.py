try:
    # Dosyayı okuma modunda açma
    with open("dosya.txt", "r") as dosya:
        # Dosyanın içeriğini okuma
        icerik = dosya.read()
        print(icerik)

except FileNotFoundError:
    print("Dosya bulunamadı.")

except:
    print("Bir hata oluştu.")