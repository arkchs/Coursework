#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd


# In[4]:


df = pd.read_csv('https://files.grouplens.org/datasets/movielens/ml-100k/u.data', sep='\t', names=['user_id','movie_id','ratings','timestamp'])


# In[8]:


user_rating_matrix = df.pivot_table(values = 'ratings', index = 'user_id', columns= 'movie_id')
user_rating_matrix.head()


# #### Use mean of given movie's ratings to fill in the missing values

# In[12]:


mean_movie_rating = user_rating_matrix.mean(axis=0) 


# In[13]:


mean_movie_rating


# In[15]:


user_rating_matrix = user_rating_matrix.replace(np.nan,mean_movie_rating)
user_rating_matrix


# In[32]:


from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
user_rating_matrix = scaler.fit_transform(user_rating_matrix)


# In[33]:


[U,S,VT] = np.linalg.svd(user_rating_matrix)


# In[34]:


S.shape


# In[35]:


VT.shape


# In[36]:


K=100
low_rank_U = U[:, :K]
low_rank_S = np.diag(S[:K])
low_rank_VT = VT[:K,:]
low_rank_approx = np.dot(np.dot(low_rank_U, low_rank_S), low_rank_VT)


# In[37]:


low_rank_approx


# #### pca and svd give same result when centered around mean

# #### S represents strength of each genre
# #### U denotes mapping of user to genres or latent features
# #### V denotes mapping of movies to users

# #### square root S into V when predicting missing values while adding it to the user mean rating

# In[44]:


sqrt_S =np.sqrt(low_rank_S)
product2= np.dot(sqrt_S ,low_rank_VT)
product1 = np.dot(low_rank_U,sqrt_S)
def predict_ratings(i,j, user_mean):
    ratings = np.dot(product1[i,:], product2[:,j])+user_mean
    return ratings


# In[45]:


user_mean_ratings = user_rating_matrix.mean(axis=1)


# In[46]:


i,j =1,2
predict_ratings(i,j,user_mean_ratings[i])


# use the VT matrix to find similarity 
# find cosine similarity of all the movies with a certain movie
# 
# 
# use dataset.make to create a dataset and implement lda
