from functools import reduce

# toplama
def toplama(x,y):
    return x+y
toplam = reduce(toplama, [1,2,3,4,5])
print(toplam) # Çıktı: 15

# çarpma
carpim = reduce(lambda x,y : x*y, [1,2,3,4,5])
print(carpim) # Çıktı: 120

# en büyük döndürme
def maksimum(x,y):
    if(x > y):
        return x
    else:
        return y
print(maksimum(3,4)) # Çıktı: 4

en_buyuk = reduce(maksimum, [-2,3,5,11])
print(en_buyuk) # Çıktı: 11