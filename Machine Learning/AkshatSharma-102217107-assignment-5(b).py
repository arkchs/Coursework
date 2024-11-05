#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df3 = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data', sep=',', names=["symboling", "normalized_losses",
"make", "fuel_type", "aspiration","num_doors", "body_style", "drive_wheels",
"engine_location", "wheel_base", "length", "width", "height", "curb_weight",
"engine_type", "num_cylinders", "engine_size", "fuel_system", "bore", "stroke",
"compression_ratio", "horsepower", "peak_rpm", "city_mpg", "highway_mpg", "price"])


# In[11]:


import numpy as np
df3.replace('?', np.NaN, inplace=True)
df3.shape
df3.isna().sum()
df3.head()


# In[12]:


df3['normalized_losses'] = df3['normalized_losses'].astype('float')
df3['bore'] = df3['bore'].astype('float')
df3['stroke'] = df3['stroke'].astype('float')
df3['horsepower'] = df3['horsepower'].astype('float')
df3['peak_rpm'] = df3['peak_rpm'].astype('float')
df3['price'] = df3['price'].astype('float')


# In[13]:


df3 = df3[df3['price'].isna()==False]
null_columns = df3.columns[df3.isnull().any() & (df3.dtypes == 'float64')]
for column in null_columns:
    df3[column].replace(np.NaN, df3[column].mean(), inplace=True)    
df3['num_doors'].fillna(df3['num_doors'].mode()[0], inplace=True)
df3['num_doors'] = df3['num_doors'].replace({'two': 2, 'four': 4, np.NaN: 0})
df3.num_cylinders.unique()
df3['num_cylinders'] = df3['num_cylinders'].replace({
    'two': 2, 
    'three': 3, 
    'four': 4, 
    'five': 5, 
    'six': 6, 
    'eight': 8, 
    'twelve': 12
})


# In[14]:


df3_encoded = pd.get_dummies(df3, columns=['body_style', 'drive_wheels'], drop_first=True)
from sklearn.preprocessing import LabelEncoder
columns_to_encode = ['make', 'aspiration', 'engine_location', 'fuel_type']
label_encoder = LabelEncoder()
for column in columns_to_encode:
    df3_encoded[column] = label_encoder.fit_transform(df3_encoded[column])


# In[15]:


df3_encoded['fuel_system'] = [1 if 'pfi' in x else 0 for x in df3_encoded['fuel_system']]

df3_encoded['engine_type'] = [1 if 'ohc' in x else 0 for x in df3_encoded['engine_type']]


# In[16]:


X_df3 = df3_encoded.drop('price', axis=1)
y_df3 = df3_encoded['price']

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_df3_scaled = scaler.fit_transform(X_df3)


# In[17]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
X_train, X_test, y_train, y_test = train_test_split(X_df3_scaled, y_df3, test_size=0.3, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
print("R-squared score on the test set:", r2)


# In[24]:


from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split

pca = PCA(n_components=0.95)  
X_pca = pca.fit_transform(X_df3_scaled)

X_train_pca, X_test_pca, y_train_pca, y_test_pca = train_test_split(X_pca, y_df3, test_size=0.3, random_state=42)

model_pca = LinearRegression()
model_pca.fit(X_train_pca, y_train_pca)

y_pred_pca = model_pca.predict(X_test_pca)
r2_pca = r2_score(y_test_pca, y_pred_pca)

print("PCA R-squared:", r2_pca)

