liste = list(filter(lambda x : x%2==0, [1,2,3,4,5,6,7,8]))
print(liste) # Çıktı: [2, 4, 6, 8]

# asal sayılar
def asal_mi(x):
    i = 2

    if(x == 1):
        return False
    elif(x == 2):
        return True
    else:
        while(i < x):
            if(x % i == 0):
                return False
            i += 1
        return True
    
liste = list(filter(asal_mi, range(1,100)))
print (liste) # Çıktı: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]