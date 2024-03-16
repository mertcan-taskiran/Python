class Kumanda():

    def __init__(self,kanal_listesi):
        self.kanal_listesi = kanal_listesi # Kanal Listemiz
        self.index = -1 # İndeksimiz
        
    def __iter__(self):
        return self # iterator oluşturduğumuzda (iter fonksiyonu çağrıldığında )objemizi döneceğiz.
    
    def __next__(self): # next fonksiyonu çağrıldığında burası çalışacak.
        self.index += 1
        if (self.index < len(self.kanal_listesi)):
            return self.kanal_listesi[self.index]
        else:
            self.index = -1
            raise StopIteration
        
kumanda = Kumanda(["Kanal 1","Kanal 2","Kanal 3","Kanal 4"]) # Objemizi oluşturuyoruz.

iterator =  iter(kumanda) # Objemiz iterable olduğu için iterator oluşturulabilir.

print(next(iterator)) # Çıktı: Kanal 1
print(next(iterator)) # Çıktı: Kanal 2
print(next(iterator)) # Çıktı: Kanal 3
print(next(iterator)) # Çıktı: Kanal 4
print(next(iterator)) # Çıktı: StopIteration