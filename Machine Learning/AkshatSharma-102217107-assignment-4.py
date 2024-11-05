#!/usr/bin/env python
# coding: utf-8

# # __Akshat Sharma 102217107__

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[5]:


df = pd.read_csv('salary_data_4.csv')
X= df['YearsExperience']
X_df = df.drop('Salary',axis=1)
Y=df['Salary']


# In[6]:


type(X)


# In[7]:


df.shape


# In[8]:


df.head()


# ### No missing values or outliers 

# In[9]:


df.isna().sum()


# In[10]:


import seaborn as sns
sns.boxplot(df['YearsExperience'])


# In[11]:


sns.boxplot(df['Salary'])


# In[12]:


plt.plot(df['YearsExperience'], df['Salary'])


# ### Manual Simple Linear Regression

# In[13]:


def error(X,Y,Bo,B1):
    error_sum=0
    for i in range(0,len(Y)):
        error_sum+=(Y[i]-(Bo+B1*X[i]))**2
    return error_sum/len(Y)


# In[32]:


def gradient(X,Y,Bo,B1):
    df_dBo=0
    df_dB1=0
    for i in range(0,len(X)):
        df_dBo += (-Y[i]+Bo+B1*X[i])
        df_dB1 += (-Y[i]*X[i]+Bo*X[i]+B1*X[i]*X[i])
    return df_dBo/len(X),df_dB1/len(X)


# In[44]:


def gradient_descent(X,Y):
    alpha = 0.01
    Bo=0
    B1=0
    mse=0
    err=0
    grad = (0,0)
    while(True):
        err = error(X,Y,Bo,B1)
        # print(err)
        grad = gradient(X,Y,Bo,B1)
        Bo -= alpha * grad[0]
        B1 -= alpha * grad[1]
        new_error = error(X,Y,Bo,B1)
        if err-new_error<1.0:
            mse=new_error
            print(new_error)
            break
    return mse


# In[45]:


mse = gradient_descent(X,Y)


# In[17]:


from sklearn.linear_model import LinearRegression
linear_reg = LinearRegression()

model = linear_reg.fit(X_df,Y)
print(model.coef_)

print(model.intercept_)

print(model.score(X_df,Y))

y = model.predict(X_df)
from sklearn.metrics import mean_squared_error
inbuilt_mse = mean_squared_error(Y,y)
print(inbuilt_mse)


# In[46]:


print(mse-inbuilt_mse)


# ### 90 10
# ### 80 20
# ### 70 30
# ### 60 40
# ### 50 50
# 

# In[49]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_df,Y,test_size=0.1,random_state=1)
from sklearn.linear_model import LinearRegression
linear_reg = LinearRegression()

model = linear_reg.fit(X_train,y_train)
y = model.predict(X_test)

from sklearn.metrics import mean_squared_error
mse10 = mean_squared_error(y_test,y)
print(mse10)
print(model.score(X_test,y_test))


# In[50]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_df,Y,test_size=0.2,random_state=1)
from sklearn.linear_model import LinearRegression
linear_reg = LinearRegression()

model = linear_reg.fit(X_train,y_train)
y = model.predict(X_test)

from sklearn.metrics import mean_squared_error
mse10 = mean_squared_error(y_test,y)
print(mse10)
print(model.score(X_test,y_test))


# In[51]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_df,Y,test_size=0.3,random_state=1)
from sklearn.linear_model import LinearRegression
linear_reg = LinearRegression()

model = linear_reg.fit(X_train,y_train)
y = model.predict(X_test)

from sklearn.metrics import mean_squared_error
mse10 = mean_squared_error(y_test,y)
print(mse10)
print(model.score(X_test,y_test))


# In[52]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_df,Y,test_size=0.4,random_state=1)
from sklearn.linear_model import LinearRegression
linear_reg = LinearRegression()

model = linear_reg.fit(X_train,y_train)
y = model.predict(X_test)

from sklearn.metrics import mean_squared_error
mse10 = mean_squared_error(y_test,y)
print(mse10)
print(model.score(X_test,y_test))


# In[53]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_df,Y,test_size=0.5,random_state=1)
from sklearn.linear_model import LinearRegression
linear_reg = LinearRegression()

model = linear_reg.fit(X_train,y_train)
y = model.predict(X_test)

from sklearn.metrics import mean_squared_error
mse10 = mean_squared_error(y_test,y)
print(mse10)
print(model.score(X_test,y_test))


# ### Create folds in the data as in create 5 folds in the data
# ### then use the first fold as the test data then second fold then the third fold and so on.
