# Örnek 1 
"""
liste1 = [1,2,3,4,5] 
liste2 = [i for i in liste1] # List Comprehension
print(liste2)
"""

# Örnek 2
"""
liste1 = [1,2,3,4,5] 
liste2 = [i*2 for i in liste1] # List Comprehension
print(liste2)
"""

# Örnek 3
"""
liste1 = [(1,2),(3,4),(5,6)]
liste2 = [i*j for (i,j) in liste1] # List Comprehension
print(liste2)
"""

# Örnek 4
"""
liste1 = [1,2,3,4,5,6,7,8,9,10]
liste2 = [i for i in liste1 if not (i == 4 or i == 9)] # List Comprehension
print(liste2)
"""

# Örnek 5
"""
s = "Python"
liste = [i * 3 for i in s] # List Comprehension
print(liste)
"""

# Örnek 6
liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste2 = [x for i in liste for x in i]
print(liste2)
