#!/usr/bin/env python
# coding: utf-8

# ## __Akshat Sharma 102217107__

# #### __Question 1__

# In[4]:


import pandas as pd
from sklearn.datasets import load_iris


# In[5]:


from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# In[6]:


iris = load_iris()
df = pd.DataFrame(iris.data, columns= iris.feature_names)
df["target"] = iris.target
df.head()


# In[7]:


from sklearn.linear_model import LogisticRegression
X = df.drop(columns=["target"])
y = df["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression(multi_class='ovr', max_iter=200)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")


# #### __Question 2__

# In[21]:


df2= pd.read_csv("weather_forecast.csv")
df2.head()


# In[22]:


df2['Rain Tomorrow (Yes/No)'] = df2['Rain Tomorrow (Yes/No)'].map({'Yes': 1, 'No': 0})
X_weather = df2.drop(columns=['Rain Tomorrow (Yes/No)'])
y_weather = df2['Rain Tomorrow (Yes/No)']


# In[30]:


df2.isnull().sum()


# In[29]:


df2.shape


# In[23]:


df2.head()


# In[28]:


X_train_weather, X_test_weather, y_train_weather, y_test_weather = train_test_split(X_weather, y_weather, test_size=0.2, random_state=42)


# In[40]:


from sklearn.tree import DecisionTreeClassifier
dt_model_weather_entropy = DecisionTreeClassifier(max_depth=5, min_samples_split=4, min_samples_leaf=2, random_state=42, criterion="entropy")
dt_model_weather_entropy.fit(X_train_weather, y_train_weather)
y_pred_weather_entropy = dt_model_weather_entropy.predict(X_test_weather)


dt_model_weather_gini = DecisionTreeClassifier(max_depth=5, min_samples_split=4, min_samples_leaf=2, random_state=42, criterion="gini")
dt_model_weather_gini.fit(X_train_weather, y_train_weather)
y_pred_weather_gini = dt_model_weather_gini.predict(X_test_weather)


dt_model_weather_log = DecisionTreeClassifier(max_depth=5, min_samples_split=4, min_samples_leaf=2, random_state=42, criterion="log_loss")
dt_model_weather_log.fit(X_train_weather, y_train_weather)
y_pred_weather_log = dt_model_weather_log.predict(X_test_weather)


# In[41]:


accuracy_weather = accuracy_score(y_test_weather, y_pred_weather_entropy)
print(f"Accuracy: {accuracy_weather:.2f}")

accuracy_weather = accuracy_score(y_test_weather, y_pred_weather_gini)
print(f"Accuracy: {accuracy_weather:.2f}")

accuracy_weather = accuracy_score(y_test_weather, y_pred_weather_log)
print(f"Accuracy: {accuracy_weather:.2f}")


# #### __Question 3__

# In[9]:


df1 = pd.read_csv("BankNote_Authentication.csv")
df1.head()


# In[11]:


X_banknote = df1.drop(columns=["class"])
y_banknote = df1["class"]


# In[ ]:


X_train_banknote, X_test_banknote, y_train_banknote, y_test_banknote = train_test_split(X_banknote, y_banknote, test_size=0.2, random_state=42)


# In[14]:


from sklearn.tree import DecisionTreeClassifier
dt_model = DecisionTreeClassifier()
dt_model.fit(X_train_banknote, y_train_banknote)
y_pred_banknote = dt_model.predict(X_test_banknote)


# In[15]:


accuracy_banknote = accuracy_score(y_test_banknote, y_pred_banknote)
print(f"Accuracy: {accuracy_banknote:.2f}")

