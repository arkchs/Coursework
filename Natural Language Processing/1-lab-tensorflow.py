#!/usr/bin/env python
# coding: utf-8

# keras, tensorflow, pytorch, lobo.
# tensors are the building blocks of tensorflow
# tensors can run on the gpu
# tensors are auto differentiable 
# tensorflow can be used for np like functions. tensors are similar to multidimensional np arrays

# In[1]:


import tensorflow as tf


# In[2]:


tf.constant([[2,3],[3,4]])


# 3 apis to create nn
# 1. sequential api: 
# 2. functional api: 
# 3. subclassing api: repeat number of layers (rnns and cnns)

# In[3]:


from tensorflow import keras
from tensorflow.keras import Sequential, layers
from tensorflow.keras.datasets import mnist


# In[4]:


(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()


# In[5]:


x_train.shape


# In[9]:


x_train = x_train.reshape(60000,784)/255


# Using Sequential API

# In[10]:


model = Sequential(
    [
        layers.Dense(512, activation='relu', input_shape=(784,), name='first_hidden_layer',),
        layers.Dense(256, activation='relu', name="second_hidden_layer",input_shape=(512,)),
        layers.Dense(10, activation='softmax',name='output_layer',input_shape=(256,))
    ]
)


# In[12]:


model.summary()


# Categorical Crossentropy: if y is a one hot vector 
# Sparse Categorical Crossentropy: if y is a single label for each class

# Optimizer:
# rmsprop: adaptive learning rate
# adam: adaptive learning rate (combination of rmsprop and gradient descent)
# sgd: stochastic gradient descent

# In[13]:


model.compile(
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
    optimizer='adam',
    metrics=["accuracy"]
)


# 938 is the number of times the weight is updated
# each iteration means that the every batch will be fed into the model once

# In[14]:


model.fit(x_train, y_train, batch_size=32, epochs=5, verbose=2)


# loss indicates the 

# In[15]:


model.evaluate(x_test.reshape(10000,784)/255, y_test, batch_size=32, verbose=2)


# In[16]:


model.predict(x_test[0].reshape(1,-1))


# In[17]:


model.summary()


# what does the first param represent. nl,nl-1
# 784*512+512=401920
# 512*256+256=131328
# 
# 
# look at this before the neural network is defined. by passing the input shape, the model is able to infer the shape of the input data. without which the model will not be able to infer the shape of the input data.
# 

# we need to use activation functions or set the logits to true in the loss function. Other wise the model will not be able to predict the output with good accuracy.

# functional is used for multiple inputs and multiple outputs for example the two digit mnist dataset

# In[ ]:




