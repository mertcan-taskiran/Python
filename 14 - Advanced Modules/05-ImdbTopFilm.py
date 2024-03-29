# Imdb Top 250 Film Verileri
import requests
from bs4 import BeautifulSoup

url = "http://www.imdb.com/chart/top"
response = requests.get(url)
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,"html.parser")

basliklar = soup.find_all("td",{"class":"titleColumn"}) # sadece adı
ratingler = soup.find_all("td",{"class","ratingColumn imdbRating"}) # sadece imdb

for baslik, rating in zip(basliklar,ratingler):
    baslik = baslik.text
    rating = rating.text

    baslik = baslik.strip()
    baslik = baslik.replace("\n","")

    rating = rating.strip()
    rating = rating.replace("\n","")

    print("Film Adı: ", baslik)
    print("Film Imdb: ", rating)
