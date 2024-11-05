#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv')


# In[3]:


df.head()


# In[5]:


X=df[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
Y=df[["species"]]


# In[20]:


df.shape


# In[7]:


import seaborn as sns
import matplotlib.pyplot as plt
sns.countplot(y="species" ,data=df, palette="viridis")
plt.xlabel("Count of each Target class")
plt.ylabel("Target classes")
plt.show()


# In[8]:


plt.figure(figsize=(15,15))


# In[9]:


p=sns.heatmap(X.corr(),annot=True,cmap='RdYlGn')


# In[11]:


from sklearn.preprocessing import StandardScaler
X_scaled = StandardScaler().fit_transform(X)
X_scaled[:5]


# In[12]:


features = X_scaled.T
cov_matrix = np.cov(features)
print(cov_matrix)


# In[13]:


values, vectors = np.linalg.eig(cov_matrix)
values[:5]


# In[14]:


explained_variances = []
for i in range(len(values)):
    explained_variances.append(values[i] / np.sum(values))
print(explained_variances)


# In[15]:


plt.figure(figsize=(6, 4))
plt.bar(range(4), explained_variances,alpha=0.5, align='center',label='individual explained variance')
plt.ylabel('Explained variance ratio')
plt.xlabel('Principal components')


# In[34]:


projected_1 = X_scaled.dot(vectors.T[0])
projected_2 = X_scaled.dot(vectors.T[1])
res = pd.DataFrame(projected_1, columns=['PC1'])
res['PC2'] = projected_2
res['Y'] = Y
res.head()


# In[35]:


plt.figure(figsize=(10,10))
X=res[["PC1","PC2"]]
p=sns.heatmap(X.corr(),annot=True,cmap='RdYlGn')


# In[36]:


res.plot(kind="scatter", x="PC1",y="PC2")


# In[16]:


X=df[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
Y=df[["species"]]
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
X_new = pca.fit_transform(X)


# In[17]:


X=df[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
Y=df[["species"]]
from scipy.linalg import svd
u,s,v= svd(X)
sigma=np.diag(s)
print(sigma)
X_new=np.dot(u[:,:4],sigma[:,:2])
print(X_new)

