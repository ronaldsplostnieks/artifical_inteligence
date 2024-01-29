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
    print(rezultats.status_code)
    if rezultats.status_code == 200:
        with open(datne, 'w', encoding='utf-8') as fails:
            fails.write(rezultats.text)
    return

# saglaba(URL, LAPAS+"pirma.html")

def dabut_info(datne):
    dati = []
    with open(datne, "r", encoding="utf-8") as f:
        html = f.read()
    
    zupa = bs(html, 'html.parser')

    galvena_dala = zupa.find(id='page_main')

    tabulas = galvena_dala.find_all('table')

    rindas = tabulas[2].find_all('tr')
    for rinda in rindas[1:-1]:
        lauki = rinda.find_all('td')

        auto = {}
        auto['sludinajuma_saite'] = lauki[1].find('a')['href']
        auto['bilde'] = lauki[1].find('img')['src']
        auto['apraksts'] = lauki[2].get_text()
        auto['marka'] = lauki[3].get_text()
        auto['gads'] = lauki[4].get_text()
        temp = lauki[5].get_text()
        if temp[-1] == 'D':
            auto['tips'] = 'Dīzelis'
            auto['tilpums'] = temp[:-1]
        elif  temp[-1] == 'E':
            auto['tips'] = 'Elektro'
            auto['tilpums'] = temp[:-1]
        elif  temp[-1] == 'H':
            auto['tips'] = 'Hibrīds'
            auto['tilpums'] = temp[:-1]
        else:
            auto['tips'] = 'Benzīns'
            auto['tilpums'] = temp  
        auto['nobraukums'] = lauki[6].get_text()
        auto['cena'] = lauki[7].get_text()
        dati.append(auto)
    return dati

def saglaba_datus(dati):
    with open(DATI+"sslv.csv", 'w', encoding="utf-8") as f:
        lauku_nosakumi = ['sludinajuma_saite', 'bilde','apraksts', 'marka', 'gads', 'tips', 'tilpums', 'nobraukums', 'cena']
        w = csv.DictWriter(f, fieldnames= lauku_nosakumi)
        w.writeheader()
        for auto in dati:
            w.writerow(auto)
        return


def atvilkt_lapas(skaits):
    for i in range(1, skaits+1):
        saglaba("{}page{}.html".format(URL, i), '{}lapas{}.html'.format(LAPAS, i))
        time.sleep(0.1)
    return

def dabut_info_visu(skaits):
    visi_dati = []
    for i in range(1, skaits):
        dati = dabut_info("{}lapa{}.html".format(LAPAS, i))
        visi_dati += dati
    return visi_dati

# atvilkt_lapas(10)
info = dabut_info_visu(10)
saglaba_datus(dabut_info(LAPAS+"pirma.html"))