#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.metrics import r2_score


# In[2]:


df = pd.read_csv('USA_Housing.csv') 
df.head()


# Divide the dataset into input features (all columns except price) and output variable
# (price)

# In[3]:


X = df.drop('Price', axis=1)
y = df['Price']


# Scale the values of input features.

# In[4]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# Divide input and output features into five folds.

# In[5]:


from sklearn.model_selection import KFold,cross_val_score
kf = KFold(n_splits=5, shuffle=True, random_state=42)


# Run five iterations, in each iteration consider one-fold as test set and remaining
# four sets as training set. Find the beta (β) matrix, predicted values, and R2_score
# for each iteration using least square error fit.

# In[6]:


from sklearn.linear_model import LinearRegression
model = LinearRegression()
cross_val_results = cross_val_score(model,X_scaled, y, cv=kf)
print(cross_val_results)


# In[7]:


from sklearn.linear_model import LinearRegression

beta_matrices = []
predicted_values_list = []
r2_scores = []

c=0
for train_index, test_index in kf.split(X_scaled):
    X_train, X_test = X_scaled[train_index], X_scaled[test_index]
    y_train, y_test = y.iloc[train_index],y.iloc[test_index]

    
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    predicted_values_list.append(y_pred)

    
    beta_matrix = pd.DataFrame(model.coef_.reshape(1, -1), columns=X.columns)
    beta_matrices.append(beta_matrix)
   
    
    r2 = r2_score(y_test, y_pred)
    r2_scores.append(r2)


best_fold_index = r2_scores.index(max(r2_scores))


best_beta_matrix = beta_matrices[best_fold_index]
best_predicted_values = predicted_values_list[best_fold_index]


print("Best Beta Matrix:\n", best_beta_matrix)


# 
# 
# 

# In[8]:


train_df = pd.DataFrame()
for i in range(5):
    if i != best_fold_index:
        train_df = pd.concat([train_df, df.iloc[train_index]])
test_df = df.iloc[test_index]

X_train_final = train_df.drop('Price', axis=1)
y_train_final = train_df['Price']
X_test_final = test_df.drop('Price', axis=1)
y_test_final = test_df['Price']


X_train_final_scaled = scaler.transform(X_train_final)
X_test_final_scaled = scaler.transform(X_test_final)

final_model = LinearRegression()
final_model.fit(X_train_final_scaled, y_train_final)


y_pred_final = final_model.predict(X_test_final_scaled)


r2_final = r2_score(y_test_final, y_pred_final)


print("R-squared score on remaining 30% data:", r2_final)


# ## __Question 2__

# ## __Temp contains 0.44 of the data, so we can set the value of test set as 30% if we use around 68 percent of the temp data. 0.44*0.6818 = 0.3__

# In[9]:


import numpy as np
from sklearn.model_selection import train_test_split

X_train, X_temp, y_train, y_temp = train_test_split(X_scaled, y, test_size=0.44, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.6818, random_state=42)


# In[10]:


def gradient_descent(X, y, alpha, iter):
    m, n = X.shape
    Beta = np.zeros(n)
    for i in range(iter):
        gradient = (1/m) * (X.T).dot(X.dot(Beta) - y)
        Beta -= alpha * gradient
    return Beta


# In[11]:


alpha = [0.001, 0.01, 0.1, 1]
iterations = 1000
best_r2_val = -np.inf
best_beta = []

for lr in alpha:
    beta = gradient_descent(X_train, y_train, lr, iterations)
    
    y_val_pred = X_val.dot(beta)
    # print(type(X_val))
    r2_val = r2_score(y_val, y_val_pred)
    
    y_test_pred = X_test.dot(beta)
    r2_test = r2_score(y_test, y_test_pred)

    print(f"Learning Rate: {lr}, R2 Score on Validation Set: {r2_val}, R2 Score on Test Set: {r2_test}")
    if r2_val > best_r2_val:
        best_r2_val = r2_val
        best_beta = beta
print("Best Regression Coefficients:\n", best_beta)

