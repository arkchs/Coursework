#!/usr/bin/env python
# coding: utf-8

# 

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


# In[ ]:


iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)        
df.head()


# In[5]:


X=iris.data
Y=iris.target


# In[ ]:


from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=42)


# In[13]:


import scipy
Y_predict=[]
import heapq
for i in range(len(X_test)):
    test_ins = X_test[i,:].reshape(1,-1)
    distance = scipy.spatial.distance.cdist(X_train, test_ins, metric="euclidean")
    nearest_indices = heapq.nsmallest(5,range(len(distance)), distance.take)
    Y_nearest_neighbours = [Y_train[k] for k in nearest_indices]
    Y_predict.append(max(set(Y_nearest_neighbours), key=Y_nearest_neighbours.count))


# In[15]:


from sklearn.metrics import classification_report
print(classification_report(Y_predict,Y_test))

