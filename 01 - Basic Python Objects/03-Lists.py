# Boş bir liste oluşturma
bos_liste = []
print(bos_liste)  # Çıktı: []

# Elemanlarla dolu bir liste oluşturma
renkler = ["kırmızı", "yeşil", "mavi"]
print(renkler)  # Çıktı: ['kırmızı', 'yeşil', 'mavi']

# Farklı veri tiplerini içeren bir liste oluşturma
farkli_tipler = [10, 3.14, "Python"]
print(farkli_tipler)  # Çıktı: [10, 3.14, 'Python']

# Belirli bir indeksteki elemana erişme
print(renkler[0])  # Çıktı: kırmızı

# Negatif indeksle elemana erişme (sondan başlayarak)
print(renkler[-1])  # Çıktı: mavi

# Belirli bir indeksteki elemanı değiştirme
renkler[1] = "sarı"
print(renkler)  # Çıktı: ['kırmızı', 'sarı', 'mavi']

# Listeye yeni bir eleman ekleme
renkler.append("turuncu")
print(renkler)  # Çıktı: ['kırmızı', 'yeşil', 'mavi', 'turuncu']

# Belirli bir indekse eleman ekleme
renkler.insert(1, "beyaz")
print(renkler)  # Çıktı: ['kırmızı', 'beyaz', 'yeşil', 'mavi', 'turuncu']

# Belirli bir indeksteki elemanı çıkarma
silinecek_renk = renkler.pop(2)
print("Silinen Renk:", silinecek_renk)  # Çıktı: Silinen Renk: yeşil
print(renkler)  # Çıktı: ['kırmızı', 'beyaz', 'mavi', 'turuncu']

# Belirli bir değere sahip tüm elemanları kaldırma
renkler.remove("beyaz")
print(renkler)  # Çıktı: ['kırmızı', 'mavi', 'turuncu']