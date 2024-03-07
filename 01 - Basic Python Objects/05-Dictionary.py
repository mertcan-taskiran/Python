# Süslü parantezler kullanarak dictionary oluşturma
ogrenci = {"ad": "Ahmet", "yas": 15, "notlar": [80, 85, 90]}
print(ogrenci)  # Çıktı: {'ad': 'Ahmet', 'yas': 15, 'notlar': [80, 85, 90]}

# dict() fonksiyonunu kullanarak dictionary oluşturma
ogrenci2 = dict(ad="Mehmet", yas=16, notlar=[75, 80, 85])
print(ogrenci2)  # Çıktı: {'ad': 'Mehmet', 'yas': 16, 'notlar': [75, 80, 85]}

# Anahtar kullanarak değere erişme
print(ogrenci["ad"])  # Çıktı: Ahmet

# get() fonksiyonuyla değere erişme
print(ogrenci.get("yas"))  # Çıktı: 15

# Eğer anahtar bulunamazsa varsayılan değeri kullanma
print(ogrenci.get("mezun", False))  # Çıktı: False

# Değerleri değiştirme
ogrenci["yas"] = 16
print(ogrenci)  # Çıktı: {'ad': 'Ahmet', 'yas': 16, 'notlar': [80, 85, 90]}

# Yeni bir anahtar-değer çifti ekleme
ogrenci["mezun"] = False
print(ogrenci)  # Çıktı: {'ad': 'Ahmet', 'yas': 16, 'notlar': [80, 85, 90], 'mezun': False}

# pop() fonksiyonuyla belirli bir anahtarın değerini silme
yas = ogrenci.pop("yas")
print("Silinen yaş:", yas)  # Çıktı: Silinen yaş: 15
print(ogrenci)  # Çıktı: {'ad': 'Ahmet', 'notlar': [80, 85, 90]}

# del anahtar_kelimesi ile belirli bir anahtarı ve değeri silme
del ogrenci["notlar"]
print(ogrenci)  # Çıktı: {'ad': 'Ahmet'}

# Sayılar ve karelerini içeren bir dictionary oluşturma
kareler = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(kareler)  # Çıktı: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# keys() metodu: Dictionary'nin anahtarlarını alır
anahtarlar = kareler.keys()
print(anahtarlar)  # Çıktı: dict_keys([1, 2, 3, 4, 5])

# values() metodu: Dictionary'nin değerlerini alır
degerler = kareler.values()
print(degerler)  # Çıktı: dict_values([1, 4, 9, 16, 25])

# items() metodu: Dictionary'nin anahtar-değer çiftlerini alır
ciftler = kareler.items()
print(ciftler)  # Çıktı: dict_items([(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)])