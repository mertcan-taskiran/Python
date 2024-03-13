liste = [1,2,2,3,3,4]
print(set(liste)) # Çıktı: {1, 2, 3, 4}

metin = "Merhaba Dünya!"
print(set(metin))

x = {"Python", "C#", "Java"}

#print(x[0]) # Error

for i in x:
    print(i)

liste = list(x)
print(liste[0])

x.add("Python") # Aynısı eklenmez
x.add("JS")
print(x)

kume1 = {1,2,3,4,5}
kume2 = {3,4,5,6,7}
print(kume2.difference(kume1))
print(kume1.difference(kume2))

kume1.discard(2) # kümeden çıkarır
print(kume1)

print(kume1.intersection(kume2)) # kesişim
print(kume1.isdisjoint(kume2)) # ortak eleman varsa false döner
print(kume1.issubset(kume2)) # alt kümesi mi?
print(kume1.union(kume2)) # birleşim kümesi oluşturur