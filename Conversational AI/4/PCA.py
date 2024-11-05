#!/usr/bin/env python
# coding: utf-8

# # Implementing PCA

# In[2]:


import numpy as np
import pandas as pd


# In[4]:


from sklearn.datasets import load_iris
iris = load_iris()


# In[7]:


iris


# In[9]:


df = pd.DataFrame(iris.data, columns=['sepal_length','sepal_width','petal_length','petal_width'])
df['target'] = iris.target


# In[11]:


df.isna().sum()


# In[19]:


get_ipython().run_line_magic('pip', 'install missingno')


# In[20]:


import missingno as msn
msn.bar(df)


# # Check for class balancing
# ### approximately each class must have same number of training examples.
# ### can use smoting technique
# ### Not required in pca as pca is unsupervised

# In[21]:


import seaborn as sns
sns.countplot(data= df, y= df['target'])


# ### Outliers are automatically removed in pca
# ### correlation is high then use feature selection or feature extraction

# In[24]:


sns.heatmap(df.iloc[:,:4].corr(), annot=True)


# #### 0.6 or lesser is acceptable
# #### Scaling matrix so that it is centered around the mean.

# In[30]:


from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df.iloc[:,:4])


# In[34]:


# covariance_matrix = np.cov(X_scaled.T)
covariance_matrix = np.cov(X_scaled,rowvar = False)


# In[39]:


values,vectors = np.linalg.eig(covariance_matrix)


# In[40]:


values


# In[38]:


vectors


# #### Explained Variance is basically the percentage across different eigen values

# In[43]:


explained_variance = []
for value in values:
    explained_variance.append((value/sum(values))*100)


# In[44]:


explained_variance


# In[47]:


column1 = np.dot(X_scaled,vectors.T[0])
column2 = np.dot(X_scaled,vectors.T[1])

result = pd.DataFrame(column1, columns=['PC1'])
result['PC2'] = column2
result['target']= df.target


# In[50]:


result


# In[56]:


sns.heatmap(result.iloc[:,:2].corr(), annot=True)


# In[51]:


result.plot(kind='scatter', x='PC1', y='PC2')


# #### Inbuilt implementation

# In[55]:


from sklearn.decomposition import PCA
pca = PCA(n_components= 2,)
pca.fit_transform(X_scaled)


# In[57]:


pca.explained_variance_ratio_

