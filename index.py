from aiohttp import request
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import time
from wsproto import Headers

URL = "https://instagram.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

def verileriAl(nickname):
    last_url = URL + nickname

    request = Request(last_url, headers=headers)

    html_verisi = urlopen(request).read()

    soup = BeautifulSoup(html_verisi, 'html.parser')

    veri = soup.find('meta', property= "og:description").attrs["content"]

    veri = veri.split("-")[0]

    veri = veri.split(" ")

    print("Takipçi sayısı: " + veri[0])
    print("Takip edilen sayısı: " + veri[2])
    print("Gönderi sayısı: " + veri[4])
    print("***********")









while True:
    secim = input("1- Kullanıcı ara\n2- Çıkış\nSeçim: ")
    if secim == "2":
        break
    else:
        if secim == "1":
            print("**********")
            nickname = input("Kullanıcı adı giriniz: ")
            verileriAl(nickname)
            time.sleep(2)
            




