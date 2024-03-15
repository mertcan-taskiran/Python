# Fonksiyonlara esnek bir şekilde argüman gönderebiliriz.

# Example 1

# def fonksiyon(*args): 
#     for i in args:
#         print(i)

# fonksiyon(1,2,3,4) # Çıktı: 1 2 3 4

# Example 2

# def fonksiyon(isim, *args):
#     print("İsim:", isim)
#     for i in args:
#         print(i)

# fonksiyon("Deneme", 1,2,3) # Çıktı: İsim:Deneme 1 2 3

# Example 3 

# def fonksiyon(**kwargs):
#     print(kwargs)

# fonksiyon(isim = "Mertcan", soyisim = "Taşkıran") # Çıktı: {'isim': 'Mertcan', 'soyisim': 'Taşkıran'}

# Example 4

# def fonksiyon(*args, **kwargs):
#     for i in args:
#         print(i)

#     for i, j in kwargs.items():
#         print(i,j)

# fonksiyon(1,2,3,4,5, isim = "Mertcan", soyisim = "Taşkıran") # Çıktı: 1 2 3 4 5 isim Mertcan soyisim Taşkıran

# Example 5

# def fonksiyon(islem_adi):
    
#     def toplama(*args):
#         toplam = 0
#         for i in args:
#             toplam += i
#         return toplam
        
#     def carpma(*args):
#         carpim = 1
#         for i in args:
#             carpim *= i
#         return carpim
    
#     if islem_adi == "toplama":
#         return toplama
#     else:
#         return carpma
    
# deneme = fonksiyon("toplama")
# print(deneme(1,2,3,4,5)) # Çıktı: 15

# deneme = fonksiyon("carpma")
# print(deneme(1,2,3,4,5)) # Çıktı: 120

# Example 6

def toplama(a,b):
    return a + b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a * b
def bölme(a,b):
    return a / b

def anafonksiyon(func1,func2,func3,func4,islem_adi): # Tanımladığımız 4 fonksiyonu da argüman olarak göndereceğiz.
    if (islem_adi == "toplama"):
        print(func1(3,4))
    elif (islem_adi == "çıkarma"):
        print(func2(10,3))
    elif (islem_adi == "çarpma"):
        print(func3(10,3))
    elif (islem_adi == "bölme"):
        print(func4(10,4))
    else:
        print("Geçersiz işlem adı...")

anafonksiyon(toplama,cikarma,carpma,bölme,"toplama") # Çıktı: 7
anafonksiyon(toplama,cikarma,carpma,bölme,"bölme") # Çıktı: 2.5