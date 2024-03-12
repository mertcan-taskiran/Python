liste = ["Elma","Armut","Muz","Kiraz"]
sonuç = list()
i = 0

for a in liste:  
    sonuç.append((i,a))
    i +=1

print(sonuç) # Çıktı: [(0, 'Elma'), (1, 'Armut'), (2, 'Muz'), (3, 'Kiraz')]

# Enumerate
liste = ["Elma","Armut","Muz","Kiraz"]
print(list(enumerate(liste))) # Çıktı: [(0, 'Elma'), (1, 'Armut'), (2, 'Muz'), (3, 'Kiraz')]