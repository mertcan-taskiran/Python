def double(x):
    return x*2
liste = list(map(double, [1,2,3,4,5]))
print(liste) # Çıktı: [2, 4, 6, 8, 10]


liste = list(map(lambda x : x**2, (1,2,3,4,5)))
print(liste) # Çıktı: [1, 4, 9, 16, 25]


liste1 = [1,2,3,4]
liste2 = [5,6,7,8]
liste = list(map(lambda x,y : x*y, liste1, liste2))
print(liste) # Çıktı: [5, 12, 21, 32]


# map() fonksiyonuyla kullanıcıdan alınan sayıların karelerini hesaplama
def kare_al(x):
    return x ** 2
sayilar = input("Lütfen bir veya daha fazla sayı girin (sayılar arasında boşluk bırakarak): ").split()
# Kullanıcıdan alınan sayıları integer'a dönüştürme
sayilar = list(map(int, sayilar))
# map() fonksiyonu ile her bir sayının karesini hesaplama
kareler = list(map(kare_al, sayilar))
print("Girilen sayıların kareleri:", kareler)