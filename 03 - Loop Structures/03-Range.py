# Belirli bir başlangıç ve bitiş değeri ile aralıktaki sayıları ekrana yazdırma
for i in range(0,10):
    print(i)

# Belirli bir başlangıç, bitiş ve adım değeri ile aralıktaki sayıları ekrana yazdırma
for i in range(1, 10, 2):
    print(i)

print(*range(10,0,-1)) # 20'den geri gelen sayıları oluşturur.

for sayı in range(1,10):
    print("* " * sayı)
