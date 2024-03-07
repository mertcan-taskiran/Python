metin = "Merhaba, Dünya!"

print(len(metin))  # Çıktı: 15

print(metin.upper())  # Çıktı: MERHABA, DÜNYA!

print(metin.lower())  # Çıktı: merhaba, dünya!

print(metin.capitalize())  # Çıktı: Merhaba, dünya!

print(metin.title())  # Çıktı: Merhaba, Dünya!

print(metin.count('a'))  # Çıktı: 3

print(metin.find('Dünya'))  # Çıktı: 9

yenimetin = metin.replace('Dünya', 'Mars')
print(yenimetin)  # Çıktı: Merhaba, Mars!

parcalar = metin.split(',')
print(parcalar)  # Çıktı: ['Merhaba', ' Dünya!']

# 4. karakterden 10. karaktere kadar olan alt dizeyi alır
alt_dize = metin[4:10]
print(alt_dize)  # Çıktı: aba, D

# İlk 5 karakteri alır
ilk_bes_karakter = metin[:5]
print(ilk_bes_karakter)  # Çıktı: Merha

# 5. karakterden sona kadar olan alt dizeyi alır
sondan_bes_onceki_karakterler = metin[-5:]
print(sondan_bes_onceki_karakterler)  # Çıktı: Dünya!

# 2'şer atlayarak metindeki karakterleri alır
iki_iki_atlayarak = metin[::2]
print(iki_iki_atlayarak)  # Çıktı: Mraa üya

# Metni ters çevirir
ters_metin = metin[::-1]
print(ters_metin)  # Çıktı: !aynüD ,abahreM

string_carpma = metin * 3
print(string_carpma) # Çıktı: Merhaba, Dünya!Merhaba, Dünya!Merhaba, Dünya!

# String toplama
a = "Python "
b = "Programlama "
c = "Dili"
print(a + b + c) # Çıktı: Python Programlama Dili


