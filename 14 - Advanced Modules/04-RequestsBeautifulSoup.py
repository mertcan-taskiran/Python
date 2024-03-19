import requests
from bs4 import BeautifulSoup

url = "web_sitesi_linki" # Site linkimiz 

response = requests.get(url) # Web sayfamızı çekiyoruz.

html_icerigi = response.content # Web sayfamızın içeriğini alıyoruz.

soup = BeautifulSoup(html_icerigi, "html.parser") # Web sayfamızı parçalamak için BeautifulSoup objesine atıyoruz.

# print(soup.prettify()) # Daha güzel bir görüntü için prettify() fonksiyonunu kullanıyoruz.

# print(soup.find_all("a")) # Bize 'a' etiketini liste şeklinde dönüyor.

# for i in soup.find_all("a"):
#     print(i.text) # 'a' etiketinin sadece text kısmını alır

print(soup.find_all("div", {"class":"deneme"})) # class ı 'deneme' olan tüm div etiketlerini alma
