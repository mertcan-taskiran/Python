#seek() fonksiyonu dosyanın başlangıcına (0 konumuna) geri döner.
#tell() fonksiyonu o anda bulunduğumuz konumu döndürür.
#Ardından, dosyanın içeriği read() fonksiyonuyla okunur. 
#tell() fonksiyonu tekrar çağrılarak dosyanın sonundaki konum alınır.

try:
    # Dosyayı okuma modunda açma
    with open("ornek_dosya.txt", "r") as dosya:
        # Dosyanın başına dön
        dosya.seek(0)

        # Dosyanın başlangıcındaki konumu al
        baslangic_konumu = dosya.tell()
        print("Başlangıç Konumu:", baslangic_konumu)

        # Dosyanın içeriğini okuma
        icerik = dosya.read()
        print("Dosya İçeriği:", icerik)

        # Dosyanın sonundaki konumu al
        son_konum = dosya.tell()
        print("Son Konum:", son_konum)

except FileNotFoundError:
    print("Dosya bulunamadı.")

except:
    print("Bir hata oluştu.")