try:
    # Kullanıcıdan iki sayı girişi alma
    sayi1 = int(input("Birinci sayıyı girin: "))
    sayi2 = int(input("İkinci sayıyı girin: "))

    # İki sayının bölümünü hesaplama
    bolum = sayi1 / sayi2
    print("İki sayının bölümü:", bolum)

# Kullanıcı doğru formatta sayı girişi yapmadığında ValueError istisnası oluşur
except ValueError:
    print("Geçersiz giriş. Lütfen bir sayı girin.")

# Sayı 0'a bölündüğünde ZeroDivisionError istisnası oluşur
except ZeroDivisionError:
    print("Sıfıra bölme hatası. İkinci sayıyı sıfırdan farklı bir değer olarak girin.")

# Farklı türde bir hata oluştuğunda genel bir hata mesajı gösterilir
except Exception as e:
    print("Bir hata oluştu:", e)

# finally bloğu her durumda çalışır
finally:
    print("Program sonlandırılıyor...")