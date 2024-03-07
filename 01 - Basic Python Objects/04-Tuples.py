# Parantez kullanarak tuple oluşturma
renkler = ("kırmızı", "yeşil", "mavi")
print(renkler)  # Çıktı: ('kırmızı', 'yeşil', 'mavi')

# Virgül kullanarak tuple oluşturma (parantez olmadan da tuple oluşturabilirsiniz)
sayilar = 1, 2, 3
print(sayilar)  # Çıktı: (1, 2, 3)

# Belirli bir indeksteki elemana erişme
print(renkler[0])  # Çıktı: kırmızı

# Negatif indeksle elemana erişme (sondan başlayarak)
print(renkler[-1])  # Çıktı: mavi

# Tuple'lar değiştirilemez (immutable) olduğundan elemanları değiştiremezsiniz
# Ancak, tuple içindeki bir liste gibi değiştirilebilir nesneler varsa, bu nesnelerin içeriği değiştirilebilir.

# renkler[0] = "turuncu"  # Hata verir

renkler_liste = list(renkler)
renkler_liste[0] = "turuncu"
renkler = tuple(renkler_liste)
print(renkler)  # Çıktı: ('turuncu', 'yeşil', 'mavi')

renkler = ("kırmızı", "yeşil", "mavi", "turuncu", "beyaz")

# Belirli bir aralıktaki elemanları dilimleme
dilim = renkler[1:4]
print(dilim)  # Çıktı: ('yeşil', 'mavi', 'turuncu')