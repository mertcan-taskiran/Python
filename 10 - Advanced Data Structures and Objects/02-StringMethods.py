metin = "Merhaba Dünya !"

print(metin.upper())
print(metin.lower())

print(metin.replace("a","x"))
print(metin.replace(" ","-"))
print(metin.replace("Merhaba","Selam"))

print(metin.startswith("M"))
print(metin.endswith("."))

print(metin.split(" "))

metin2 = "-----Python-----"
print(metin2.strip("-"))
print(metin2.lstrip("-"))
print(metin2.rstrip("-"))

liste = ["01","01","1998"]
print("/".join(liste))

print(metin.count("a"))
print(metin.count(" "))

print(metin.find("a"))
print(metin.find("x"))
print(metin.rfind("a"))