# Liste de gezinme
liste = [1,2,3,4,5,6,7]

for eleman in liste:
    print("Eleman",eleman)

# Liste elemanlarını toplama
liste = [1,2,3,4,5,6,7]
toplam = 0
for eleman in liste:
    toplam += eleman
print("Toplam",toplam)

# Çift elemanları bastırma
liste = [1,2,3,4,5,6,7,8,9]

for eleman in liste:
    if eleman % 2 == 0:
        print(eleman)

# Karakter Dizileri Üzerinde Gezinmek
s =  "Python"
for karakter in s:
    print(karakter)

# Her bir karakterleri 3 ile çarpma
for karakter in s:
    print(karakter * 3)

# Demetler üzerinde gezinmek 
demet =  (1,2,3,4,5,6,7)

for eleman in demet:
    print(eleman)

# Listeler için 2 boyutlu demetler

liste = [(1,2),(3,4),(5,6),(7,8)]

for eleman in liste:
    print(eleman)

# Demet içindeki herbir elemanı almak için pratik yöntem
liste = [(1,2),(3,4),(5,6),(7,8)]

for (i,j) in liste:
    print(i,j)

# Sözlükler üzerinde gezinmek

# Metodları kullanmadan sözlük üzerinde gezinmek - Sadece anahtarları alabiliyoruz.
sözlük = {"bir":1,"iki":2,"üç":3,"dört":4}

for eleman in sözlük:
    print(eleman)

# keys()
for eleman in sözlük.keys():
    print(eleman)

# values() 
for eleman in sözlük.values():
    print(eleman)

# items() 
for (i,j) in sözlük.items():
    print("Anahtar:",i," - ","Değer:",j)