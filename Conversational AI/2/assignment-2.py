#!/usr/bin/env python
# coding: utf-8

# 

# In[2]:


import requests
import pandas as pd


# In[45]:


company_names=['apple inc','videocon','intel']
for company in company_names:
    base_url = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords='+company+'&apikey='+API_KEY
    res = requests.get(base_url)
    data = res.json()   
    print(data.get('bestMatches')[0]['1. symbol']+':'+data.get('bestMatches')[0]['2. name'])


# In[46]:


base_url1 = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AAPL&interval=15min&outputsize=full&apikey='+API_KEY
res1 = requests.get(base_url1)
data1 = res1.json()   

print(data1)


# In[48]:


data1.get('Time Series (15min)')


# In[47]:


base_url2 = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=511389.BSE&outputsize=compact&apikey='+API_KEY
res2 = requests.get(base_url2)
data2 = res2.json()   

print(data2)


# In[50]:


len(data2.get('Time Series (Daily)'))


# In[35]:


base_url3 = 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=IBM&apikey='+API_KEY
res3 = requests.get(base_url3)
data3 = res3.json()
# print(data3)


# In[39]:


listData3 = data3.get('feed')
print(listData3[0]['title'])
print(listData3[0]['summary'])
print(listData3[0]['authors'])
print(listData3[0]['overall_sentiment_score'])
print(listData3[0]['overall_sentiment_label'])


# In[29]:


base_url4 = 'https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey='+API_KEY
res4 = requests.get(base_url4)
data4 = res4.json()

print(data4)


# In[34]:


listData4_0 = data4.get('top_gainers')
listData4_1 = data4.get('top_losers')
listData4_2 = data4.get('most_actively_traded')
for i in range(len(listData4_0)):
    print(listData4_0[i]['ticker']+' '+listData4_1[i]['ticker']+' '+listData4_2[i]['ticker'])


# In[19]:


base_url5 = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=IBM&apikey='+API_KEY
res5 = requests.get(base_url5)
data5 = res5.json()

# print(data5)


# In[27]:


listData5_0 = data5.get('annualReports')
count=5
for d in listData5_0:
    if count==0: break
    count-=1
    print(d['netIncome'])
print('\n')
listData5_1  = data5.get('quarterlyReports')
for d in listData5_1:
    if count==5: break
    count+=1
    print(d['netIncome'])


# In[16]:


base_url6 = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=INR&apikey='+API_KEY
res6 = requests.get(base_url6)
data6 = res6.json()

print(data6)


# In[18]:


print(data6.get('Realtime Currency Exchange Rate')['5. Exchange Rate'])

