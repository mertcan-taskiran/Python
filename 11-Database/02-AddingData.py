import sqlite3 # Sqlite'yı dahil ediyoruz

con = sqlite3.connect("11-Database/database.db") # Tabloya bağlanıyoruz.

cursor = con.cursor() # cursor isimli değişken veritabanı üzerinde işlem yapmak için kullanacağımız imleç olacak.

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, director TEXT, imdb DOUBLE, duration INT)") # Sorguyu çalıştırıyoruz. id adında bir sütun ekler ve bu sütun otomatik olarak artan bir şekilde ayarlanır.
    con.commit() # Sorgunun veritabanı üzerinde geçerli olması için commit işlemi gerekli.

tablo_olustur()


    
def veri_ekle(name,director,imdb,duration):
    cursor.execute("INSERT INTO movies VALUES(?,?,?,?)", (name, director, imdb, duration))
    con.commit()

# veri_ekle('Harry Potter','JK Rowling',9.8,140)

# Kullanıcıdan alma
def veri_ekle2(name, director, imdb, duration):
    cursor.execute("INSERT INTO movies (name, director, imdb, duration) VALUES (?, ?, ?, ?)", (name, director, imdb, duration))
    con.commit()

name = input("Film Adı: ")
director = input("Director: ")
imdb = float(input("Imdb: "))
duration = int(input("Duration: "))

veri_ekle2(name, director, imdb, duration)


con.close() # Bağlantıyı koparıyoruz.