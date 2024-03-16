"""
Generator fonksiyonlar, her bir değeri bellekte saklamak yerine ihtiyaç duyulduğunda ürettikleri için bellek kullanımında daha verimlidirler. 
Bu nedenle büyük veri kümeleri üzerinde çalışırken generator'ları tercih etmek genellikle daha iyi bir seçenektir.
"""

def karelerial():
    for i in range(1,6):
        yield i ** 2 # yield anahtar kelimesi generator'un değer üretmesi için kullanılıyor.
generator =  karelerial()

print(generator) # Generator objesi

iterator = iter(generator)

print(next(iterator)) # Çıktı: 1 değeri üretildi
print(next(iterator)) # Çıktı: 4 değeri üretildi 1 değeri tarihe karıştı.
print(next(iterator)) # Çıktı: 9 değeri üretildi 4 değeri tarihe karıştı.
print(next(iterator)) # Çıktı: 16 değeri üretildi 9 değeri tarihe karıştı
print(next(iterator)) # Çıktı: 25 değeri üretildi 16 değeri tarihe karıştı.
#print(next(iterator)) # Çıktı: StopIteration. Üretilecek değer kalmadı.

# Çarpım Tablosu
def carpimtablosu():
    for i in range(1,11):
        for j in range(1,11):
            yield "{} x {} = {}".format(i,j,i*j)
for i in carpimtablosu():
    print(i)