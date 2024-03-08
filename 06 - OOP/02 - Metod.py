class Araba:
    def __init__(self, marka, model, renk, hiz=0):
        self.marka = marka
        self.model = model
        self.renk = renk
        self.hiz = hiz
    
    def calistir(self):
        print(f"{self.marka} {self.model} çalıştı.")
    
    def hizlan(self, artis):
        self.hiz += artis
        print(f"{self.marka} {self.model}'in hızı {self.hiz} km/s'ye çıktı.")
    
    def yavasla(self, azalis):
        self.hiz -= azalis
        print(f"{self.marka} {self.model}'in hızı {self.hiz} km/s'ye düştü.")

    def dur(self):
        self.hiz = 0
        print(f"{self.marka} {self.model} durdu.")
        
# Araba sınıfından bir nesne oluşturma
araba1 = Araba("BMW", "X", "Beyaz")

# Arabayı çalıştırma
araba1.calistir()

# Arabanın hızını artırma ve azaltma
araba1.hizlan(20)
araba1.yavasla(10)

# Arabayı durdurma
araba1.dur()

