liste = [1,2,3,4,5]
liste.append(6)
print(liste) # Çıktı: [1, 2, 3, 4, 5, 6]

liste2 = [7,8,9]
liste.extend(liste2)
print(liste) # Çıktı: [1, 2, 3, 4, 5, 6, 7, 8, 9]

liste.insert(2, "Python")
print(liste) # Çıktı: [1, 2, 'Python', 3, 4, 5, 6, 7, 8, 9]

print(liste.pop()) # Çıktı: 9
print(liste.pop(2)) # Çıktı: Python

liste.remove(1)
print(liste) # Çıktı: [2, 3, 4, 5, 6, 7, 8]

liste = [1,2,3,4,5]
index = liste.index(3)
print(index) # Çıktı: 2

liste = [3,1,2,2,3,3,3,4,5]
print(liste.count(3)) # Çıktı: 4

liste.sort()
print(liste) # Çıktı: [1, 2, 2, 3, 3, 3, 3, 4, 5]