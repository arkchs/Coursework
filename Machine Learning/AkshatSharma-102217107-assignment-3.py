#!/usr/bin/env python
# coding: utf-8

# # __Akshat Sharma 102217107__

# In[42]:


from sklearn.datasets import load_digits
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd


# In[43]:


digits = load_digits()
X = digits.data
y = digits.target
df = pd.DataFrame(data=digits.data, columns=digits.feature_names)
df['target_number'] = y


# In[44]:


df.head()
# df.shape


# In[45]:


import seaborn as sns
import matplotlib.pyplot as plt
sns.countplot(y="target_number",data=df,palette='viridis')
plt.xlabel("Count of samples")
plt.ylabel("Numbers")
plt.show()


# In[73]:


plt.figure(figsize=(30,30))
sns.heatmap(df.loc[:,df.columns!='target_numbers'].head(100).corr(), annot=True, cmap='RdYlGn')


# In[58]:


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled[:1]#view one of the elements


# In[56]:


cov_matrix = np.cov(X_scaled.T)
print(cov_matrix)


# In[49]:


eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)


# In[50]:


sorted_index = np.argsort(eigenvalues)[::-1]#descending order of eigenvalues trick
sorted_eigenvalues = eigenvalues[sorted_index]
sorted_eigenvectors = eigenvectors[:, sorted_index]


# In[59]:


explained_variances = []
for i in range(len(eigenvalues)):
    explained_variances.append(eigenvalues[i] / np.sum(eigenvalues))
print(explained_variances)


# In[61]:


plt.figure(figsize=(6, 4))
plt.bar(range(64), explained_variances,alpha=0.5, align='center',label='individual explained variance')
plt.ylabel('Explained variance ratio')
plt.xlabel('Principal components')


# In[64]:


projected_1 = X_scaled.dot(eigenvectors.T[0])
projected_2 = X_scaled.dot(eigenvectors.T[1])
res = pd.DataFrame(projected_1, columns=['PC1'])
res['Y'] = y
res.head()


# In[69]:


res.plot(kind="scatter", x="PC1",y="PC2")


# # __Using Inbuilt Functions__

# In[53]:


pca = PCA(n_components=2)
X_reduced_inbuilt = pca.fit_transform(X_scaled)

