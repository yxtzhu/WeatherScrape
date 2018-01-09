
# coding: utf-8

# # Toronto Historical Weather Web Scraping

# In[469]:

#Import libraries
import urllib.request
from bs4 import BeautifulSoup


# In[470]:

#Government of Canada Website 
page = 'http://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=51459&timeframe=2&StartYear=1840&EndYear=2018&Day=7&Year=2018&Month=1#'


# In[471]:

#Query the website
f=urllib.request.urlopen(page).read()


# In[472]:

#Parse the page using beautiful soup
soup = BeautifulSoup(f, 'html.parser')
print(type(soup))


# In[633]:

#print(soup.prettify)


# In[634]:

#Find the option for year and month
option = soup.find_all('div', class_='col-md-6 col-sm-6 col-xs-6 text-center mrgn-tp-md mrgn-bttm-md')


# In[635]:

option=option[0]
print(option)


# In[636]:

option=option.find_all('option', selected=True)
print(option)


# In[637]:

year=option[0]
year=year.find(text=True)
print(year)


# In[638]:

month=option[1]
month=month.find(text=True)
print(month)


# In[640]:

#Find the table
#table = soup.find_all('div', class_='table-responsive')
table = soup.find_all('table')


# In[641]:

print(type(table))


# In[642]:

th_all = soup.find_all('th')
result = []
for th in th_all:
    result.append(th.find('abbr', text=True))

title=[]
for abbr in result:
    if abbr is not None:
        title.append(abbr.string)
    
print(title)


# In[643]:

#clean up title
for i in range(len(title)):
    if title[i]=='mm':
        title[i]="Total Rain"
    elif title[i]=='cm':
        title[i]="Total Snow"
print(title)


# In[674]:

table_body = soup.find('tbody')
tr = table_body.find_all('tr')
td=[]
date=[]
data=[]
for row in tr:
    d=[]
    for r in row.find_all('td'):
        date.append(r.find('abbr'))
        d.append(r.string)
    data.append(d)
print(data)


# In[675]:

#clean date arrays
t=[]
for d in date:
  if d is not None:
    t.append(d.get('title'))
print(t)


# In[676]:

from datetime import datetime
date=[]
for j in t:
    date.append(datetime.strptime(j, '%B %d, %Y'))
print(date)


# In[679]:

#clean up data array
for entry in data:
    if entry == []:
        data.remove(entry)
    else:
        if len(entry)>11:
            entry.pop(0)
                
for rm in range(len(data)-len(date)):
    data.pop(len(data)-1)
    rm -=1
print(data)


# In[692]:

for r in range(len(data)):
    for c in range(len(data[r])):
        if data[r][c] is not None:
            data[r][c]=float(data[r][c])
print(data)


# In[693]:

for rm in range(len(title)-len(data[0])):
    title.pop(len(title)-1)
    rm-=1
print(title)


# In[696]:

#Construct dataframe for scraped data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df = pd.DataFrame(data=data,index=date,columns=title)
print(df)


# In[756]:

plt.figure(figsize=(20, 10)); plt.plot(date, data); plt.legend(title);plt.title('Toronto Weather Data Jan 2018');


# In[ ]:




# In[ ]:




# In[ ]:



