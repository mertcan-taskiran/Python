import random
import time

print("""************************

Sayi Tahmin Oyunu


1 ile 1000 arasinda sayiyi tahmin edin.

************************""")

rastgele_sayi = random.randint(1,1000)
tahmin_hakki = 10
while True:

    tahmin = int(input("Tahmininiz:"))
    if (tahmin < rastgele_sayi):
        time.sleep(1)
        print("Daha yüksek bir sayi söyleyin....")
        tahmin_hakki -= 1
    elif (tahmin > rastgele_sayi):
        time.sleep(1)
        print("Daha düşük bir sayi söyleyin....")
        tahmin_hakki -= 1
    else:
        time.sleep(1)
        print("Tebrikler! Sayimiz",rastgele_sayi)
        break
    if (tahmin_hakki == 0):
        print("Tahmin Hakkiniz Bitti...")
        print("Sayimiz:",rastgele_sayi)
        break