
# coding: utf-8

# # Toronto Historical Weather Web Scraping

# In[12]:

#Import libraries
import urllib.request
from bs4 import BeautifulSoup


# In[13]:

#Government of Canada Website 
page = 'http://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=51459&timeframe=2&StartYear=1840&EndYear=2018&Day=7&Year=2018&Month=1#'


# In[40]:

#Query the website
f=urllib.request.urlopen(page).read()


# In[43]:

#Parse the page using beautiful soup
soup = BeautifulSoup(f, 'html.parser')
print(type(soup))


# In[46]:

print(soup.prettify)


# In[87]:

#Find the option for year and month
option = soup.find_all('div', class_='col-md-6 col-sm-6 col-xs-6 text-center mrgn-tp-md mrgn-bttm-md')
print(option)


# In[88]:

option=option[0]
print(option)


# In[90]:

option=option.find_all('option', selected=True)
print(option)


# In[96]:

year=option[0]
year=year.find(text=True)
print(year)
   


# In[97]:

month=option[1]
month=month.find(text=True)
print(month)


# In[98]:

#Find the table
table = soup.find_all('div', class_='table-responsive')
print(table)


# In[ ]:




# In[ ]:



