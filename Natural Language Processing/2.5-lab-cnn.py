#!/usr/bin/env python
# coding: utf-8

# output of a convolutional layer must be maintained as the same therefore we use padding to make sure the 
# 
# 
# pooling layer = function is to reduce dimensionality and still keep the important features. It is used to reduce the computational cost and to some extent also reduce overfitting. It is also used to extract dominant features which are rotational and positional invariant.
# filter shape 
# max pooling and average pooling is used to reduce dimensionality.
# 
# stride = how much the filter moves each time. let say the filter window moves faster and skips certain strips of pixels. also helps with contrasting.

# batch normalization: normalizes the output of a previous activation layer by subtracting the batch mean and dividing by the batch standard deviation. It is used to make the model faster and more stable.

# In[97]:


import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, BatchNormalization
from tensorflow.keras.datasets import cifar10


# In[98]:


(x_train, y_train), (x_test, y_test) = cifar10.load_data()

y_train = y_train.reshape(-1,)
y_test = y_test.reshape(-1,)


# In[99]:


import matplotlib.pyplot as plt


# In[100]:


outputs = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]


# In[101]:


def disp_img(index):
    plt.imshow(x_train[index])
    plt.xlabel(outputs[y_train[index]])


# In[102]:


disp_img(10)


# In[103]:


x_train = x_train.reshape(-1, 32*32*3)/255.0
x_test = x_test.reshape(-1, 32*32*3)/255.0


# In[104]:


from sklearn.model_selection import train_test_split
x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, random_state=42, test_size=0.2)


# In[105]:


y_train.shape


# In[110]:


class MyModel(keras.Model):
    def __init__(self,):
        super(MyModel, self).__init__()
        self.input = layers.Flatten
        self.dense1 = layers.Dense(100, activation='relu')
        self.dense2 = layers.Dense(50, activation = 'relu')
        self.dense3 = layers.Dense(10, activation='softmax')
    def call(self , inputs):
        x=self.dense1(inputs)
        x=self.dense2(x)
        x=self.dense3(x)
        return x
model = MyModel()


# In[111]:


model.compile(
    loss = keras.losses.SparseCategoricalCrossentropy(),
    optimizer = keras.optimizers.Adam(learning_rate=0.01) , 
    metrics= ['accuracy'], 
)


model.fit(x_train, y_train, batch_size=64, epochs=5, validation_data=(x_val, y_val))

