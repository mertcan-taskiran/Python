# Ana sınıf (Üst sınıf)
class Calisan:
    def __init__(self, ad, soyad, maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas

    def bilgileri_goster(self):
        print("Adı:", self.ad)
        print("Soyadı:", self.soyad)
        print("Maaşı:", self.maas)

# Alt sınıf (Alt sınıf), Calisan sınıfından kalıtım alıyor
class Mudur(Calisan):
    def __init__(self, ad, soyad, maas, bolum):
        super().__init__(ad, soyad, maas)
        self.bolum = bolum

    def bilgileri_goster(self):
        super().bilgileri_goster()
        print("Bölümü:", self.bolum)

# Alt sınıf (Alt sınıf), Calisan sınıfından kalıtım alıyor
class Programci(Calisan):
    def __init__(self, ad, soyad, maas, diller):
        super().__init__(ad, soyad, maas)
        self.diller = diller

    def bilgileri_goster(self):
        super().bilgileri_goster()
        print("Bildiği Diller:", ", ".join(self.diller))

# Mudur ve Programci sınıflarından nesneler oluşturma
mudur1 = Mudur("Mert", "Taş", 10000, "İnsan Kaynakları")
programci1 = Programci("Can", "Kıran", 8000, ["Python", "Java", "C#"])

# Nesnelerin bilgilerini gösterme
print("--- Müdür Bilgileri ---")
mudur1.bilgileri_goster()
print("\n--- Programcı Bilgileri ---")
programci1.bilgileri_goster()
