#!/usr/bin/env python
# coding: utf-8

# # __Akshat Sharma 102217107__

# In[2]:


get_ipython().run_line_magic('pip', 'install opendatasets')
get_ipython().run_line_magic('pip', 'install pandas')


# In[3]:


import pandas as pd
import opendatasets as od


# In[4]:


od.download("https://www.kaggle.com/jahias/microsoft-adventure-works-cycles-customer-data")


# ##Creating a dataframe and viewing the first five entries.

# In[5]:


file = ("microsoft-adventure-works-cycles-customer-data/AWCustomers.csv")
df = pd.read_csv(file)
df.head()


# In[6]:


import matplotlib.pyplot as plt
plt.hist(df['LastUpdated'])


# In[7]:


sales_file = ("microsoft-adventure-works-cycles-customer-data/AWSales.csv")
df_sales = pd.read_csv(sales_file)
df_sales.head()


# ## What does the title column represent?

# In[8]:


# df.size
print(df.shape[0])
df_not_null_title = df[pd.notnull(df["Title"])]
df_not_null_title.head()
df.columns


# # __Analysis of Features for Selection__
# ##    1. CustomerID is essential as it connects both the csvs
# ##    2. BirthDate can be used to acquire the age of a certain person which can be useful for predicting the age groups that buy cycles the most.
# ##    3. NumberChildrenAtHome is more important than TotalChildren as it is more likely for children at home to receive the cycle as a present
# ##    4. Yearly Income is crucial whereas LastUpdated is not as important.
# **********************************************************************
# ## 1. Title is not useful as gender can provide the same information and gender itself is also not useful in determining the buying probability.
# ## 2. The 'FirstName', 'MiddleName', 'LastName', 'Suffix', 'AddressLine1', 'AddressLine2', 'City', 'StateProvinceName','CountryRegionName', 'PostalCode', 'PhoneNumber'. does not matter either as it doesn't reveal the customers' willingness to buy a certain commodity.
# ## 3. Education and Occupation do not matter as much either
# ## 4. MaritalStatus, HomeOwnerFlag does not matter
# 

# In[9]:


dropped_features = [ 'Title', 'FirstName', 'MiddleName', 'LastName', 'Suffix',
       'AddressLine1', 'AddressLine2', 'City', 'StateProvinceName',
       'CountryRegionName', 'PostalCode', 'PhoneNumber','Occupation','Education',
        'Gender', 'MaritalStatus', 'HomeOwnerFlag',
        'TotalChildren',
        'LastUpdated']

df_sf = df.drop(columns=dropped_features)
df_sf.head()


# 

# ## CustomerID: Discrete Interval
# ## BikerBuyer: Discrete Binary
# ## NumberCarsOwned: Discrete Ratio
# ## NumberChildrenAtHome: Discrete Ratio
# ## YearlyIncome: Discrete Ratio
# ## AvgMonthSpend: Continuous Ratio
# ## BirthDate: Discrete Interval

# In[10]:


df_joined = pd.merge(df_sf,df_sales,on='CustomerID')
df_joined.head()


# In[11]:


import numpy as np
print(len(df_joined['AvgMonthSpend']))
range = np.linspace(start=0,stop=18360, num=100)
plt.plot(range, df_joined['AvgMonthSpend'].head(100), color='red', linestyle='dashed', marker='o', label='Avg Month Spend')
plt.xlabel('Index')
plt.ylabel('Average Monthly Spend')
plt.title('Average Monthly Spend vs. Index')
plt.legend()
plt.grid(True)
plt.show()


# # __Dealing With NULL values__
# 

# In[12]:


df_joined.isna().sum()


# # __Normalization__

# In[13]:


from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

scaled_data_ams = scaler.fit_transform(df_joined[['AvgMonthSpend']])
scaled_data_yi = scaler.fit_transform(df_joined[['YearlyIncome']])
df_joined['AvgMonthSpend'] = scaled_data_ams.flatten()
df_joined['YearlyIncome'] = scaled_data_yi.flatten()


# In[14]:


df_joined.head()


# 

# # __Converting the Birth Date Column to extract the age of customers__

# In[15]:


import datetime

def calculate_age_in_years(birth_date):
  born = datetime.datetime.strptime(birth_date, "%Y-%m-%d")
  today = datetime.date.today()
  age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
  return age

df_joined['Age'] = df_joined['BirthDate'].apply(calculate_age_in_years)
scaler = MinMaxScaler()
df_joined['Age'] = scaler.fit_transform(df_joined[['Age']])
df_joined.drop(columns = ['BirthDate', 'CustomerID'], inplace=True)
df_joined.head()


# # __Discretization based on Equal Width Binning__

# In[16]:


df_joined['YearlyIncome'] = pd.cut(df_joined['YearlyIncome'], bins=10, labels=[1,2,3,4,5,6,7,8,9,10])
df_joined['Age'] = pd.cut(df_joined['Age'], bins=10, labels=[.1,.2,.3,.4,.5,.6,.7,.8,.9,1.0])

df_joined.head()


# # __Standardization of the AvgMonthSpend column__

# In[17]:


from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df_joined['AvgMonthSpend'] = scaler.fit_transform(df_joined[['AvgMonthSpend']])
df_joined['YearlyIncome'] = scaler.fit_transform(df_joined[['YearlyIncome']])

df_joined.head()


# # __Binarization of Categorical Data__

# In[18]:


from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder()
encoded_data = encoder.fit_transform(df_joined[['NumberChildrenAtHome']])
encoded_df = pd.DataFrame(encoded_data.toarray(), columns=encoder.get_feature_names_out())


# In[19]:


df_joined = pd.concat([df_joined,encoded_df],axis=1)
df_joined.drop(columns=['NumberChildrenAtHome'],inplace=True)
df_joined.head()


# # __Simple Matching, Jaccard, Cosine Similarity for the Number Of Children At Home__

# In[20]:


def simple_matching_coefficient(row1, row2):
  matching_columns = np.sum(row1 == row2)
  total_columns = len(row1)
  return matching_columns / total_columns

def jaccard_similarity(col1, col2):
  intersection = (col1 == col2).sum()
  union = len(col1) + len(col2) - intersection
  return intersection / union

def cosine_similarity(a, b):
  dot_product = np.dot(a, b)
  norm_a = np.linalg.norm(a)
  norm_b = np.linalg.norm(b)
  return dot_product / (norm_a * norm_b)




df_only_ncah = df_joined.drop(columns=['NumberCarsOwned','YearlyIncome','BikeBuyer','AvgMonthSpend','Age'])
row1 = df_only_ncah.iloc[0].values
row2 = df_only_ncah.iloc[1].values
print(simple_matching_coefficient(row1,row2))
print(cosine_similarity(row1,row2))#it is zero 'cause the values are completely unrelated to each other
print(jaccard_similarity(row1,row2))


# # __Correlation between Number of Cars Owned and Yearly Income__

# In[21]:


correlation = df_joined['NumberCarsOwned'].corr(df_joined['YearlyIncome'])
print(correlation)

