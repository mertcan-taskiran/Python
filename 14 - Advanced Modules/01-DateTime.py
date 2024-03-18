from datetime import datetime

simdi = datetime.now()
print(simdi) # Çıktı: 2024-03-18 15:35:46.079764

print(simdi.year) # Çıktı: 2024
print(simdi.month) # Çıktı: 3
print(simdi.day) # Çıktı: 18

print(datetime.ctime(simdi)) # Çıktı: Mon Mar 18 15:37:52 2024

"""
strftime() fonksiyonu

    Yıl bilgisini almak için : %Y
    
    Ay ismini almak için : %B

    Gün ismini almak için : %A

    Saat bilgisini almak için : %X

    Gün bilgisini almak için : %D
"""

print(datetime.strftime(simdi,"%Y")) # Çıktı: 2024
print(datetime.strftime(simdi,"%B")) # Çıktı: March
print(datetime.strftime(simdi,"%A")) # Çıktı: Monday
print(datetime.strftime(simdi,"%X")) # Çıktı: 15:39:48
print(datetime.strftime(simdi,"%D")) # Çıktı: 03/18/24
print(datetime.strftime(simdi,"%Y %B")) # Çıktı: 2024 March
print(datetime.strftime(simdi,"%Y %B %A")) # Çıktı: 2024 March Monday

"""
Şu anki zamanı saniye cinsinden bulmak için, datetime objemizi timestamp() fonksiyonumuza gönderebiliriz. 
Aynı zamanda saniye cinsinden verilmiş bir zamanı da fromtimestamp fonksiyonuyla datetime objesine çevirebiliriz.
"""

saniye =  datetime.timestamp(simdi)
print(saniye) # Çıktı: 1710765956.641792
zaman =  datetime.fromtimestamp(saniye)
print(zaman) # Çıktı: 2024-03-18 15:45:56.641792


# iki tarih arasındaki farkı bulmak
tarih = datetime(2024,1,1) 
fark = simdi - tarih
print(fark)