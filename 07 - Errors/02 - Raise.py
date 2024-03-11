def kontrol_et(sayi):

    if sayi < 0:
        # Eğer sayı negatifse, ValueError istisnası oluşturulur
        raise ValueError("Negatif sayılar kabul edilmez.")
    else:
        print("Girilen sayı pozitif.")

try:
    # Kullanıcıdan bir sayı girişi alınır
    sayi = int(input("Bir sayı girin: "))
    # Kontrol fonksiyonu çağrılır
    kontrol_et(sayi)

except ValueError:
    # Hata mesajı gösterilir
    print("Negatif sayılar kabul edilmez.")
