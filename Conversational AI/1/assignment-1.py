#!/usr/bin/env python
# coding: utf-8

# # __Akshat Sharma 102217107__

# In[33]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[34]:


url = "https://timesofindia.indiatimes.com/home/headlines"
req = requests.get(url)
if(req.status_code==200):
    print("we can go ahead")
html_content = req.content
soup = BeautifulSoup(html_content,'html.parser')
# print(soup.prettify)


# In[35]:


df = pd.DataFrame(columns=["title", "link"])
datalist=[]


# In[36]:


prefix = 'https://timesofindia.com'
all_data = soup.find_all('span', attrs={'class': 'w_tle'})
print(all_data)
count=10
for data in all_data:
    datalist=[]
    if count==0: 
        break
    title = data.text
    if(title==None):
        datalist.append('NaN')
    else:
        datalist.append(title)

    link = data.find('a').get('href')
    if(link==None):
        datalist.append('NaN')
    else:
        datalist.append(prefix+link)
    df.loc[len(df)] = datalist
    count-=1


# In[37]:


df.head()


# # __LinkedIn scraping__

# In[59]:


search_query = "Software Engineer"
search_location = "New York"#mapped to the geoId of 115918472
mod_query = search_query.replace(' ','%20')
mod_loc = search_location.replace(' ', '%20')
print(mod_query)


# In[61]:


url = "https://www.linkedin.com/jobs/search?keywords="+mod_query+"&location="+mod_loc+"&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
req = requests.get(url)
print(url)
if(req.status_code==200):
    print('we can go ahead')
html_content = req.content
soup = BeautifulSoup(html_content, 'html.parser')
soup.prettify


# # __Avoid parsing the html document in the following manner as it takes a higher amount of compute__

# In[ ]:


job_listings = soup.find_all('span',attrs ={'class':'sr-only'})
all_data = soup.find_all('a',attrs={'class': 'base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]'})
all_data_company = soup.find_all('h4', attrs={'class': 'base-search-card__subtitle'})


# # __Better Way__

# In[64]:


all_data_better = soup.find_all('div', attrs={'class': 'base-search-card__info'})
# print(all_data_better)
df=pd.DataFrame(columns=['job_title','company', 'job_app_link'])
for data in all_data_better:
    row=[]
    temp = data.find('h3',attrs={'class': 'base-search-card__title'})
    if(temp==None): row.append('NaN')
    else:
        row.append(temp.text)
    # print(temp.text)
    temp2 = data.find('h4',attrs={'class': 'base-search-card__subtitle'})
    if(temp2==None): row.append('NaN')
    else: row.append(temp2.text)
    # print(temp2.text)
    temp3 = data.find('a',attrs={'class':'hidden-nested-link'})
    # print(temp3.get('href'))
    if(temp3==None): row.append('NaN')
    else: row.append(temp3.get('href'))
    df.loc[len(df)] = row


# In[63]:


# df.to_csv('output2.csv')
df.head()

