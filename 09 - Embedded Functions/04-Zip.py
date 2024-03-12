liste1 = [1,2,3,4,5]
liste2 = [6,7,8,9,10,11]

i = 0
sonuc = list()
while (i < len(liste1) and i < len(liste2)):
    sonuc.append((liste1[i],liste2[i]))
    i +=1

print(sonuc) # Çıktı: [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]

# Zip ile yapalım.
liste1 = [1,2,3,4,5]
liste2 = [6,7,8,9,10,11]

liste = list(zip(liste1,liste2))
print(liste) # Çıktı: [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]

# Aynı anda iki liste üzerinde gezinmek
liste1 = [1,2,3,4]
liste2 = ["Python","Php","Java","Javascript"]

for i,j in zip(liste1,liste2):
    print("i:",i,"j:",j)

# Sözlük üzerinde gezinmek
sözlük1 = {"Elma":1,"Armut":2,"Kiraz":3}
sözlük2 = {"Sıfır":0,"Bir":1,"İki":2}

liste = list(zip(sözlük1,sözlük2)) # Anahtarlar eşleşti.
print(liste)

liste = list(zip(sözlük1.values(),sözlük2.values())) # Değerler eşleşti
print(liste)