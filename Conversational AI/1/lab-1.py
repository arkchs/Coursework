#!/usr/bin/env python
# coding: utf-8

# # Beautiful Soup vs Selenium vs Scrapy
# bs creates the parse tree and parsers can then be chosen. 

# In[4]:


get_ipython().run_line_magic('pip', 'install requests')
get_ipython().run_line_magic('pip', 'install html5lib')
get_ipython().run_line_magic('pip', 'install bs4')


# In[78]:


import requests
from bs4 import BeautifulSoup
#from [library] import [class]
import pandas as pd


# In[84]:


pageno=1

url = "https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_"+str(pageno)+"_books?ie=UTF8&pg="+str(pageno)
req = requests.get(url) #get the html of the target url
if(req.status_code==200):
    print('we can go ahead') 
    #break otherwise
html_content=req.content 
#types of parsing a document
soup=BeautifulSoup(html_content,'html.parser')
print(soup.prettify)

# book_name = 
# author_name = 
# ratings = 
# votes = 
# book_type= 
# book_link = 


# In[86]:


df = pd.DataFrame(columns= ['Book Name', 'Author Name', 'Ratings', 'Votes', 'Book type', 'Book link'])
book_data =[]
for d in soup.find_all('div', attrs={'class':'zg-grid-general-faceout'}):
    book_name = d.find('div',attrs={'class': '_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y'})
    if(book_name == None):
        book_data.append('NaN')
    else:
        book_data.append(book_name)
    author_name = d.find('div',attrs={'class': 'a-row a-size-small'})
    if(author_name == None):
        book_data.append('NaN')
    else:
        book_data.append(author_name)
    ratings = d.find('span',attrs={'class':'a-icon-alt'})
    if(ratings == None):
        book_data.append('NaN')
    else:
        book_data.append(ratings)
    votes = d.find('span',attrs={'class':'a-size-small'})
    if(votes == None):
        book_data.append('NaN')
    else:
        book_data.append(votes)
    book_type = d.find('span', attrs={'class': 'a-size-small a-color-secondary a-text-normal'})
    if(book_type== None):
        book_data.append('NaN')
    else:
        book_data.append(book_type)
    link = d.find('a',attrs={'class':'a-link-normal aok-block'})
    rel_link =link.get('href')
    complete_link = 'amazon.in'+rel_link
    if(complete_link== None):
        book_data.append('NaN')
    else:
        book_data.append(complete_link)
    df.loc[len(df)] = (book_data)


# In[44]:


soup.find('title')
soup.find_all('a')
soup.find_parent('body')


# In[ ]:





# # locate a particular anchor tag 
# 

# In[50]:


soup.find_all('a',attrs={'class': 'skip-link'})
soup.find_parent('a',attrs={'class':'skip-link'})
soup.find_parents()# finds all the nodes above the first occurence of that very element.
soup.find('title').text
soup.find('title')


# In[79]:





# # Find the times of india headline page and get the top ten headlines and the link to read that article
# # __Linkedin and find the job title and link to apply for the job and also make an interface keyword and location__
