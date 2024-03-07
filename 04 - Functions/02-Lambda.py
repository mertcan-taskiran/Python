# İki sayıyı toplayan bir lambda ifadesi
toplama = lambda x, y: x + y
print(toplama(3, 5))  # Çıktı: 8

# Bir sayının karesini hesaplayan bir lambda ifadesi
kare = lambda x: x ** 2
print(kare(4))  # Çıktı: 16

# Verilen bir stringin uzunluğunu döndüren bir lambda ifadesi
uzunluk = lambda s: len(s)
print(uzunluk("Python"))  # Çıktı: 6

# İki sayının çarpımını hesaplayan bir lambda ifadesi
carpim = lambda x, y: x * y
print(carpim(3, 5))  # Çıktı: 15

# Çift mi tek mi lambda ifadesi
cifttek = lambda sayi : sayi % 2 == 0
print(cifttek(14))