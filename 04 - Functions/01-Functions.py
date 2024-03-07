# İki sayıyı toplayan bir fonksiyon
def toplama(a, b):
    return a + b

print(toplama(3, 5))  # Çıktı: 8


# Bir stringin uzunluğunu döndüren bir metot
def uzunluk(string):
    return len(string)

print(uzunluk("Python"))  # Çıktı: 6

# Bir listedeki en büyük sayıyı bulan bir metot
def en_buyuk(liste):
    return max(liste)

print(en_buyuk([3, 5, 9, 2, 7]))  # Çıktı: 9