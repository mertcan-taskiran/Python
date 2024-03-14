import sqlite3 # Sqlite'yı dahil ediyoruz

con = sqlite3.connect("11-Database/database.db") # Tabloya bağlanıyoruz.

cursor = con.cursor() # cursor isimli değişken veritabanı üzerinde işlem yapmak için kullanacağımız imleç olacak.

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS movies (name TEXT, director TEXT, imdb DOUBLE, duration INT)") # Sorguyu çalıştırıyoruz.
    con.commit() # Sorgunun veritabanı üzerinde geçerli olması için commit işlemi gerekli.

tablo_olustur()

con.close() # Bağlantıyı koparıyoruz.