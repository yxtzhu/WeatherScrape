# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def ScrapeWeather(page):
    
    #Query the website

    f=urllib.request.urlopen(page).read()
    
    #Parse the page using beautiful soup
    soup = BeautifulSoup(f, 'html.parser')
    
    #Find the section that contains the year and the month
    option = soup.find_all('div', class_='col-md-6 col-sm-6 col-xs-6 text-center mrgn-tp-md mrgn-bttm-md')
    option=option[0]
    option=option.find_all('option', selected=True)
       
    #Find title
    th_all = soup.find_all('th')
    result = []
    for th in th_all:
        result.append(th.find('abbr', text=True))

    title=[]
    for abbr in result:
        if abbr is not None:
            title.append(abbr.string)
            
    #clean up title
    for i in range(len(title)):
        if title[i]=='mm':
            title[i]="Total Rain"
        elif title[i]=='cm':
            title[i]="Total Snow"
    
    #Find data
    table_body = soup.find('tbody')
    tr = table_body.find_all('tr')
    date=[]
    data=[]
    for row in tr:
        d=[]
        for r in row.find_all('td'):
            date.append(r.find('abbr'))
            d.append(r.string)
        data.append(d)
    
    #clean date arrays
    t=[]
    for d in date:
        if d is not None:
            t.append(d.get('title'))
    
    date=[]
    for j in t:
        date.append(datetime.strptime(j, '%B %d, %Y'))

    #clean up data array
    for entry in data:
        if entry == []:
            data.remove(entry)

    for entry in data:
        if len(entry)>11:
            entry.pop(0)

    #There should be as many rows as the number dates
    for rm in range(len(data)-len(date)):
        data.pop(len(data)-1)
        rm -=1
    
    for rm in range(len(title)-len(data[0])):
        title.pop(len(title)-1)
        rm-=1
    
    #Construct dataframe for scraped data
    df = pd.DataFrame(data=data,index=date,columns=title)
    df=df.apply(pd.to_numeric, errors="coerce")
    
    return df
