import os

print(os.getcwd()) # Hangi dizinde bulunuyor.

print(os.listdir()) # Bulunduğumuz dizindeki klasör ve dosyalar sıralanır.

print(os.mkdir("Deneme")) # Deneme adında klasör oluşturur.

print(os.makedirs("Deneme1/Deneme2")) # Yazılan yol ile klasör oluşturur.

print(os.rmdir("Deneme1/Deneme2")) # Siler.

print(os.removedirs("Deneme1/Deneme2")) # Tüm alt dizinleri de siler.

print(os.rename("deneme.txt", "deneme2.txt")) # Yeniden adlandırır.