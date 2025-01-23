#!/usr/bin/env python
# coding: utf-8

# In[11]:


import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.datasets import mnist


# In[21]:


(x_train, y_train), (x_test, y_test) = mnist.load_data()
print(x_train.shape)
x_train = x_train.reshape(-1, 28*28).astype('float32') / 255.0
x_test = x_test.reshape(-1, 28*28).astype('float32') / 255.0


# In[13]:


from sklearn.model_selection import train_test_split
x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.2, random_state=42)


# in this model we dont need Functional API  as the there is only one input and one output.
# 

# In[16]:


input = keras.Input(shape=(784,))
x= layers.Dense(512, activation='relu')(input)
x =layers.Dense(256, activation='relu')(x)
output = layers.Dense(10, activation='softmax')(x)

model = keras.Model(inputs=input, outputs = output)


# In[17]:


model.compile(loss=keras.losses.SparseCategoricalCrossentropy(), optimizer= keras.optimizers.Adam(learning_rate=0.01),
               metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=64, epochs=32, validation_data=(x_val, y_val))


# Learning about subclassing now

# In[20]:


class MyModel(keras.Model):
    def __init__(self, num_classes=10):
        super(MyModel, self).__init__()
        self.dense1 = layers.Dense(512, activation='relu')
        self.dense2 = layers.Dense(256, activation='relu')#number of neurons and the activation
        self.dense3 = layers.Dense(num_classes, activation='softmax')#number of output labels and activation for the output layer

    def call(self, inputs):
        #taking the self object and the inputs taken as a tensor for the first layer inputs
        x = self.dense1(inputs)
        x = self.dense2(x)
        x=self.dense3(x)
model1 = MyModel()


# In[19]:


model.compile(loss=keras.losses.SparseCategoricalCrossentropy(), optimizer= keras.optimizers.Adam(learning_rate=0.01)
              , metrics=['accuracy'])
model.fit(x_train, y_train, batch_size=64, epochs=5, validation_data=(x_val, y_val))


# Neural Network arch is of 1000 layers and 10 lines are repeating with the same code and in that case subclassing is the best way to go.
# 
# save weights saves the current weight so far and allows continuing the same weight parameters on another session.
# save model saves the entire arch with the weights and allows to continue the training from the same point. in case of some further aspect for improvement.

# In[ ]:


model.save_weights('./weights/model')

