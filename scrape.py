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
        if lauki[1].find('a')['href'] != " ":
            auto['sludinajuma_saite'] = "https://www.ss.lv/"+lauki[1].find('a')['href']+" "
        else:
            auto['sludinajuma_saite'] = " "

        if lauki[1].find('img')['src'] != " ":
            auto['bilde'] = lauki[1].find('img')['src']+" "
        else:
            auto['bilde'] = " "

        if lauki[2].get_text() != " ":
            apraksts_temp = lauki[2].find('a').get_text()
            apraksts_temp = apraksts_temp.replace("\t", "").replace("\r", "").replace("\n", "")
            auto['apraksts'] = apraksts_temp
        else:
            auto['apraksts'] = " "

        if lauki[3].get_text() != " ":
            auto['marka'] = lauki[3].get_text()
        else:
            auto['marka'] = " "

        if lauki[4].get_text() != " ":
            auto['gads'] = lauki[4].get_text()
        else:
            auto['gads'] = " "
        if lauki[5].get_text != " ":
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
        else: 
            auto['tips'] = " "
            auto['tilpums'] = " "

        if lauki[6].get_text() != " ":
            auto['nobraukums'] = lauki[6].get_text()
        else:
            auto['nobraukums'] = " "

        if lauki[7].get_text() != " ":
            auto['cena'] = lauki[7].get_text()
        else:
            auto['cena'] = " "
        dati.append(auto)
    return dati

def saglaba_datus(dati):
    with open(DATI+"sslv.csv", "w", encoding='utf-8') as f:
        lauku_nosaukumi = ['sludinajuma_saite','bilde', 'apraksts', 'marka', 'gads', 'tips', 'tilpums', 'nobraukums', 'cena']
        w = csv.DictWriter(f, fieldnames= lauku_nosaukumi)
        w.writeheader()
        for auto in dati:
            w.writerow(auto)
    return



def atvilkt_lapas(skaits):
    for i in range(1,skaits+1):
        saglaba("{}page{}.html".format(URL, i), "{}lapa{}.html".format(LAPAS, i))
        time.sleep(1)
    return


def dabut_info_daudz(skaits):
    visi_dati = []
    for i in range(1, skaits+1):
        dati = dabut_info("{}lapa{}.html".format(LAPAS,i))
        visi_dati += dati
    return visi_dati

# atvilkt_lapas(5)
info = dabut_info_daudz(5)
saglaba_datus(info)