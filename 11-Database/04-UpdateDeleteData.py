import sqlite3

# Create Table

con = sqlite3.connect("11-Database/database.db")
cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, director TEXT, imdb DOUBLE, duration INT)")
    con.commit()

tablo_olustur()

# Add Data

def veri_ekle(name, director, imdb, duration):
    cursor.execute("INSERT INTO movies (name, director, imdb, duration) VALUES (?, ?, ?, ?)", (name, director, imdb, duration))
    con.commit()

name = input("Film Adı: ")
director = input("Director: ")
imdb = float(input("Imdb: "))
duration = int(input("Duration: "))

veri_ekle(name, director, imdb, duration)

# Get Data

def veri_al():
    cursor.execute("Select * From movies")
    liste = cursor.fetchall()
    print("--- Film Listesi ---")
    for i in liste:
        print(i)

veri_al()

# Update Data

def veri_guncelle(eski_deger, yeni_deger):
    cursor.execute("Update movies set director = ? where director = ?", (yeni_deger, eski_deger))
    con.commit()

veri_guncelle("Rowling", "J.K Rowling")

# Delete Data

def veri_sil(film_adi):
    cursor.execute("Delete From movies where name = ?", (film_adi,))
    con.commit()

veri_sil("Felsefe Taşı")


con.close()