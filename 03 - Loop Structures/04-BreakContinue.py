"""
i = 0
while (i < 20):
    print(i)
    if (i == 10):
        break # i'nin değeri 10 olunca bu koşul sağlanıyor ve  break ifadesiyle karşılaşıldığı için döngü anında sona eriyor.
    i +=1
"""
"""
while True: # Sonsuz döngü.
    isim = input("İsminiz(Çıkmak için q tuşuna basın.):")
    if (isim == "q"):
        print("Çıkış yapılıyor...")
        break
    print(isim)
"""
"""
liste = [1,2,3,4,5,6,7,8,9]
for i in liste:
    if (i == 3 or i == 5):
        continue
    print("i:",i)
"""