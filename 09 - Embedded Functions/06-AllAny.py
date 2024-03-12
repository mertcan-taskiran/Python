# Bütün değerler True ise True, en az birisi False ise False döner.
def hepsi(liste): 

    for i in liste:
        if not i:
            return False
    return True

liste = [True,False,True,False,True]
print(hepsi(liste))

# Herhangi bir değer True ise True, Hepsi False ise False döner.
def herhangi(liste):

    for i in liste:
        if i:
            return True
    return False

liste = [True,False,True,False,True]
print(hepsi(liste))

liste = [0,0,0,0,0,0,0] # Bütün değerler False , 0 = False
print(herhangi(liste))

# All ve Any

# all() fonksiyonu bütün değerler True ise True, en az bir değer False ise False sonuç döndürür.
liste = [True,True,True,True,True]
print(all(liste))

# any() fonksiyonu bütün değerler False ise False, en az bir değer True ise True sonuç döndürür.
liste = [True,False,True,False,True]
print(any(liste))