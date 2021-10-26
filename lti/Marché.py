#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# -*- coding : utf8 -*-
# author : HOUMMANI Ayoub
# Webscraping module




from os import error
import requests
import json
from bs4 import BeautifulSoup
import lxml
import pandas as pd
import datetime 

class Data:
    #Private class instance:

    __symbols = pd.DataFrame([['Addoha P', 'MA0000011512'],
       ['AFMA P', 'MA0000012296'],
       ['Afric Indus.', 'MA0000012114'],
       ['Afriquia Gaz P', 'MA0000010951'],
       ['Agma P', 'MA0000010944'],
       ['Alliances P', 'MA0000011819'],
       ['Aluminium Maroc P', 'MA0000010936'],
       ['Aradei Capital Br', 'MA0000012460'],
       ['ATLANTASANAD P', 'MA0000011710'],
       ['Attijariwafa Bk Rg', 'MA0000012445'],
       ['Auto Hall P', 'MA0000010969'],
       ['Auto Nejma P', 'MA0000011009'],
       ['BALIMA P', 'MA0000011991'],
       ['BoA Br', 'MA0000012437'],
       ['BCP P', 'MA0000011884'],
       ['BMCI P', 'MA0000010811'],
       ['Cartier Saada P', 'MA0000011868'],
       ['CDM P', 'MA0000010381'],
       ['Central.Danone P/N', 'MA0000012049'],
       ['CIH P', 'MA0000011454'],
       ['Ciments Maroc', 'MA0000010506'],
       ['CMT', 'MA0000011793'],
       ['Colorado P', 'MA0000011934'],
       ['COSUMAR', 'MA0000012247'],
       ['CTM P', 'MA0000010340'],
       ['Dari Couspate', 'MA0000011421'],
       ['Delattre Lev. P', 'MA0000011777'],
       ['Delta Holding P', 'MA0000011850'],
       ['Diac Salaf P', 'MA0000010639'],
       ['DISWAY P', 'MA0000011637'],
       ['Ennakl N', 'MA0000011942'],
       ['EQDOM P', 'MA0000010357'],
       ['FENIE BROSSETTE P', 'MA0000011587'],
       ['HPS P', 'MA0000011611'],
       ['IBMaroc.com P', 'MA0000011132'],
       ['Immr Invest Br', 'MA0000012387'],
       ['INVOLYS P', 'MA0000011579'],
       ['Jet Contractors P', 'MA0000012080'],
       ['LABEL VIE P', 'MA0000011801'],
       ['LafargeHolcim Ma Br', 'MA0000012320'],
       ['Lesieur Cristal', 'MA0000012031'],
       ['Lydec P', 'MA0000011439'],
       ['M2M Group P', 'MA0000011678'],
       ['Maghreb Oxygene P', 'MA0000010985'],
       ['Maghrebail P', 'MA0000011215'],
       ['Managem P', 'MA0000011058'],
       ['Maroc Leasing N', 'MA0000010035'],
       ['Maroc Telecom', 'MA0000011488'],
       ['Med Paper P', 'MA0000011447'],
       ['Microdata N', 'MA0000012163'],
       ['Mutandis Br', 'MA0000012395'],
       ['Nexans Maroc P', 'MA0000011140'],
       ['Oulmes P', 'MA0000010415'],
       ['PROMOPHARM', 'MA0000011660'],
       ['Rebab Company P', 'MA0000010993'],
       ['Res.Dar Saada Br', 'MA0000012239'],
       ['Risma P', 'MA0000011462'],
       ['S2M P', 'MA0000012106'],
       ['Saham Assurance N', 'MA0000012007'],
       ['SALAFIN P', 'MA0000011744'],
       ['SAMIR P', 'MA0000010803'],
       ['SMI P', 'MA0000010068'],
       ['Stokvis Nord Afr.', 'MA0000011843'],
       ['SNEP P', 'MA0000011728'],
       ['Sonasid P', 'MA0000010019'],
       ['SOTHEMA', 'MA0000011645'],
       ['SRM P', 'MA0000011595'],
       ['Ste Boissons P', 'MA0000010365'],
       ['STROC Indus. P', 'MA0000012056'],
       ['SODEP P', 'MA0000012312'],
       ['TAQA Morocco P', 'MA0000012205'],
       ['Timar P', 'MA0000011686'],
       ['Total Maroc P', 'MA0000012262'],
       ['Unimer P', 'MA0000012023'],
       ['Wafa Assur P', 'MA0000010928'],
       ['Zellidja P', 'MA0000010571']], columns=['name','ISIN'], dtype='string')
    
    __symbols.index = __symbols['ISIN']
    __symbols.drop('ISIN', axis=1, inplace=True)

    def __init__(self):
        return None

    def getsymbols():
        print(Data.__symbols)

    
    def GetToday():

        link = 'https://www.leboursier.ma/component/option,com_api/format,json/lang,fr/method,getBasicStocksInfo/view,api/'
        page = requests.get(link)
        bSoup = BeautifulSoup(page.text, features='lxml') 
        tab = json.loads(bSoup.text.encode().decode('utf-8-sig'))['result']
        tab = pd.DataFrame(tab)
        tab.drop('ISIN', axis = 1, inplace=True)
        tab = tab.astype({'name':'string', 'cours':'float', 'variation':'float'})
        tab.index = tab['name']
        tab.drop('name',axis=1, inplace=True)
        
        return tab

    def GetSingleData(name, start=None, end=None):

        ISIN = Data.__symbols.loc[Data.__symbols['name']==name].index[0]
        link = 'https://www.leboursier.ma/api?method=getStockOHLC&ISIN='+ ISIN +'&format=json'
        
        page = requests.get(link)
        bSoup = BeautifulSoup(page.text, features='lxml') 
        tab = json.loads(bSoup.text.encode().decode('utf-8-sig'))['result']
        tab = pd.DataFrame(tab)
        tab.index = tab[0].apply(lambda x: str(datetime.datetime.fromtimestamp(x//1000).date()))
        tab.index.name = 'Date'
        tab.drop(0, axis = 1, inplace=True)
        tab.columns = ['Open', 'High', 'Low', 'Close','Volume']
        
        return tab[start:end].iloc[::-1]

    def MasiComposition():

        link = 'http://www.casablanca-bourse.com/bourseweb/indice-ponderation.aspx?Cat=22&IdLink=298'
        page = requests.get(link)
        bSoup = BeautifulSoup(page.text, 'lxml')   
        content =bSoup.find('table').find_all('span')
        ISIN = []
        Instr = []
        Poids =[]
        for i in range(11, len(content)-9, 8):
            ISIN.append(content[i].text)
            Instr.append(content[i+1].text)
            Poids.append(float(content[i+7].text.replace(',','.')))
        names = []
        for i in range(len(ISIN)):
            try:
                names.append(Data.__symbols.loc[ISIN[i]][0])
            except KeyError:
                names.append(Instr[i])

        bd = pd.DataFrame({'poids':Poids, 'symbols':names,'BVC_symb':Instr}, index = ISIN)

        return bd

    def GetManyData(*args, start= None, end=None):
        data = {}
        erros = []
        for name in args:
            try:
                data[name] = Data.GetSingleData(name, start=start, end=end)

            except IndexError:
                erros.append(name)
                pass
        if len(erros) > 0:
            print('Errors : ', erros, 'Are not handled by this library')
                
        return data

    def GetIndex(name='Masi', start = None, end=None):
        # MASI and MADEX
        if (name =='Masi'):
            ISIN_MASI = 'MA0000000050'
            link = 'https://www.leboursier.ma/api?method=getMasiHistory&format=json'
        if (name=='Madex'):
            ISIN_MADEX = 'MA0000000053'
            link = 'https://www.leboursier.ma/component/option,com_api/ISIN,'+ ISIN_MADEX +'/format,json/lang,fr/method,getMadexOHLC/view,api/'    


        cont = requests.get(link)
        bSoup = BeautifulSoup(cont.text, 'lxml') 
        tab = json.loads(bSoup.text.encode().decode('utf-8-sig'))['result']
        tab = pd.DataFrame(tab)
        tab.index = tab[0].apply(lambda x: str(datetime.datetime.fromtimestamp(x//1000).date()))
        tab.index.name = 'Date'
        tab.drop([0,5], axis = 1, inplace=True)
        tab.columns = ['Open', 'High', 'Low', 'Close']
        return tab[start:end]

