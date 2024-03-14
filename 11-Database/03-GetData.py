import sqlite3

con = sqlite3.connect("11-Database/database.db")

cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, director TEXT, imdb DOUBLE, duration INT)")
    con.commit()

tablo_olustur()

def veri_ekle(name, director, imdb, duration):
    cursor.execute("INSERT INTO movies (name, director, imdb, duration) VALUES (?, ?, ?, ?)", (name, director, imdb, duration))
    con.commit()

# name = input("Film Adı: ")
# director = input("Director: ")
# imdb = float(input("Imdb: "))
# duration = int(input("Duration: "))

# veri_ekle(name, director, imdb, duration)

def veri_al():
    cursor.execute("Select * From movies")
    liste = cursor.fetchall()
    print("--- Film Listesi ---")
    for i in liste:
        print(i)

veri_al()

con.close()