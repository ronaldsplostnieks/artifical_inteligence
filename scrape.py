import requests
import os
from bs4 import BeautifulSoup as bs
import csv
import time

URL = "https://www.ss.lv/lv/transport/cars/today-5/sell/"
LAPAS = "lapas/"
DATI = "dati/"

def saglaba(url, datne):
    rezultats = requests.get(url)
    if rezultats.status_code == 200:
        with open(datne, "w", encoding = 'utf-8') as fails:
            fails.write(rezultats.text)
    return

def dabut_info(datne):
    dati = []
    with open(datne, "r", encoding="UTF-8")as f:
        html = f.read()
    zupa = bs(html, 'html.parser')

    galvena_dala = zupa.find(id='page_main')

    tabulas = galvena_dala.find_all('table')

    rindas = tabulas[2].find_all('tr')

    for rinda in rindas[1:]:
        lauki = rinda.find_all('td')
        print(lauki)
        auto = {}
        auto['sludinajums_saite'] = lauki[1].find('a')['href']
        print(auto['sludinajums_saite'])

# saglaba(URL, LAPAS+"pirma.html")
dabut_info("lapas/pirma.html")