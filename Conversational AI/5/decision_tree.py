#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np


# In[11]:


df = pd.read_csv("weather.csv")
df.head()


# In[12]:


df.shape


# In[13]:


def find_entropy(df):
    target= df.keys()[-1]
    target_values = df[target].unique() # number of different classes in the target column
    entropy = 0
    for value in target_values:
        prob = len(df[df[target]==value])/len(df)+1e-7 # probability of each class
        entropy += -prob*np.log2(prob)
    return entropy


# #### __Example is from the slides__

# In[14]:


find_entropy(df) 


# In[ ]:


def find_avg_info_entropy(df,attribute):
    attr_values = df[attribute].unique()
    target = df.keys()[-1]
    target_values = df[target].unique()
    avg_info_entropy = 0
    for value in attr_values:
        entropy_subsample = 0
        for value1 in target_values:
            num = len(df[attribute][df[attribute]==value][df[target]==value1])
            den = len(df[attribute][df[attribute]==value])
            prob = num/den
            entropy_subsample += (-prob*np.log2(prob+1e-7))# adding a small number to avoid 0 entropy problem
        weight = len(df[attribute][df[attribute]==value])/len(df)
        avg_info_entropy += weight*entropy_subsample
    return avg_info_entropy     


# 

# In[16]:


find_avg_info_entropy(df, 'Outlook')


# In[17]:


def find_winner(df):
    attributes = df.keys()[:-1]
    IG=[]
    for attribute in attributes:
        IG.append(find_entropy(df)-find_avg_info_entropy(df,attribute))
    return attributes[np.argmax(IG)] # argmax returns the index of the largest value


# In[18]:


find_winner(df)


# In[19]:


def training(df,tree=None):
    root = find_winner(df)
    target = df.keys()[-1]
    if tree is None:
        tree={}
        tree[root] = {}
    root_values = df[root].unique()
    for value in root_values:
        sub_df = df[df[root]==value].reset_index(drop=True) # dropping the index column if the drop = False then the indexes are created to be [1,2,3,4] for [5,7,12,15]
        values, counts = np.unique(sub_df[target], return_counts=True)
        if(len(counts)==1):
            tree[root][value]=values[0]
        else:
            tree[root][value]=training(sub_df)
    return tree


# In[20]:


tree = training(df)


# In[21]:


import pprint
pprint.pprint(tree)


# In[22]:


def prediction(tree, instance):
    root = tree.keys()
    value = instance[root]
    sub_tree = tree[root][value]
    label = 0
    if type(sub_tree) is dict:
        label = prediction(sub_tree, instance)
    else:
        label = sub_tree
    return label


# In[23]:


df1 = pd.read_csv("weather_test.csv")
df1.head()

