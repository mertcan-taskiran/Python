# Numpy, Python programlama dilinde bilimsel hesaplamalar için kullanılan güçlü bir kütüphanedir. 
# Çok boyutlu diziler ve matrisler üzerinde yüksek performanslı matematiksel işlemler yapmamızı sağlar.
# Ayrıca bu işlemler için geniş bir matematiksel fonksiyon ve rastgele sayı üreteci koleksiyonu sunar.

# data_list = [1,2,3]
# print(data_list) # Çıktı: [1, 2, 3]

import numpy as np

# arr = np.array(data_list)
# print(arr) # Çıktı: [1 2 3]

# data_list2 = [[10,20,30],[40,50,60],[70,80,90]]
# arr2 = np.array(data_list2)
# print(arr2) 
# Çıktı: 
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]]

# print(arr[1]) # Çıktı: 2
# print(arr2[1][1]) # Çıktı: 50

# print(np.arange(10,20)) # Çıktı: [10 11 12 13 14 15 16 17 18 19]
# print(np.arange(10,20,3)) # Çıktı: [10 13 16 19]
# print(np.zeros(10)) # Çıktı: [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
# print(np.ones(10)) # Çıktı: [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

# print(np.zeros((2,2))) 
# Çıktı: 
# [[0. 0.]
#  [0. 0.]]

# print(np.ones((2,2))) 
# Çıktı: 
# [[1. 1.]
#  [1. 1.]]

# print(np.linspace(0,100,5)) # Çıktı: [  0.  25.  50.  75. 100.]

# print(np.eye(3))
# Çıktı: 
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# print(np.random.randint(0,10)) # Çıktı: random sayı
# print(np.random.randint(0,10,3)) # Çıktı: 3 random sayılı array

# arr = np.arange(9)
# print(arr.reshape(3,3))
# Çıktı: 
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

# newArray = np.random.randint(1,100,10)
# print(newArray)
# print(newArray.max())
# print(newArray.min())
# print(newArray.sum()) # Tüm değerlerin toplamı
# print(newArray.mean()) # Ortalama Bulur 
# print(newArray.argmin()) # En küçük eleman indeksi
# print(newArray.argmax()) # En büyük eleman indeksi

# detArray =  np.random.randint(1,100,9)
# print(detArray.reshape(3,3))

# arr = np.arange(0,10)
# print(arr[1:5]) # Çıktı: [1 2 3 4]
# print(arr[::2]) # Çıktı: [0 2 4 6 8]

# arr = np.arange(0,10)
# arr2 = arr.copy() 
# print(arr2) # Çıktı: [0 1 2 3 4 5 6 7 8 9]
# arr2[:3] = 25
# print(arr2) # Çıktı: [25 25 25  3  4  5  6  7  8  9]
# print(arr) # Çıktı: [0 1 2 3 4 5 6 7 8 9]

# arr = np.arange(1,10)
# print(arr > 2) # Çıktı: [False False  True  True  True  True  True  True  True]
# print(arr[arr > 5]) # Çıktı: [6 7 8 9]

# arr1 = np.array([10,20,30,40,50])
# arr2 = np.array([2,3,4,5,6])
# print(arr1 + arr2) # Çıktı: [12 23 34 45 56]
# print(arr1 * arr2) # Çıktı: [ 20  60 120 200 300]
# print(arr1 / 3) # Çıktı: [ 3.33333333  6.66666667 10.         13.33333333 16.66666667]
# print(arr2 ** 2) # Çıktı: [ 4  9 16 25 36]