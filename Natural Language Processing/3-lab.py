#!/usr/bin/env python
# coding: utf-8

# In[16]:


import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, Sequential
from tensorflow.keras.layers import Flatten, Dense, BatchNormalization, MaxPooling2D, Conv2D


# In[17]:


from tensorflow.keras.datasets import cifar10


# In[18]:


(x_train, y_train), (x_test, y_test) = cifar10.load_data()


# In[19]:


print(x_train.shape)


# This is normalization

# In[20]:


x_train = x_train/255.0
x_test = x_test/255.0


# In[21]:


from sklearn.model_selection import train_test_split
x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.2, random_state=42)


# In[22]:


model=Sequential()
model.add(keras.Input(shape=(32,32,3)))
model.add(Conv2D(32,3,  activation='relu'))
model.add(MaxPooling2D(2))
model.add(Conv2D(64,3,  activation='relu'))
model.add(MaxPooling2D(2))
model.add(Conv2D(128,3,  activation='relu'))
model.add(MaxPooling2D(2))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(10, activation='softmax'))


# In[23]:


model.summary()


# In[24]:


model.compile(optimizer=keras.optimizers.Adam(3e-4), loss=keras.losses.SparseCategoricalCrossentropy(), metrics=['accuracy'])


# In[25]:


model.fit(x_train, y_train, batch_size=64, epochs=10, validation_data=(x_val, y_val))


# In[13]:


#Functional API
inputs = keras.Input(shape=(32,32,3))
x = Conv2D(32,3,)(inputs) #32 channels of filters and 3x3 kernel(size of filter applied) then can also mention the stride
x = BatchNormalization()(x)# ensure to do batch normalization before adding the relu
x=keras.activations.relu(x)
x=MaxPooling2D(2)(x)


x = Conv2D(64,3,)(inputs) 
x = BatchNormalization()(x)
x=keras.activations.relu(x)
x=MaxPooling2D(2)(x)


x = Conv2D(128,3,)(inputs) 
x = BatchNormalization()(x)
x=keras.activations.relu(x)
x=MaxPooling2D(2)(x)


x=Flatten()(x)

x=Dense(64, activation='relu')(x)
outputs = Dense(10, activation ='softmax')(x)

model1 = keras.Model(inputs =inputs , outputs = outputs)


# In[14]:


model1.compile(optimizer=keras.optimizers.Adam(3e-4), loss=keras.losses.SparseCategoricalCrossentropy(), metrics=['accuracy'])


# Using batch normalization can lead to overfitting problem. why?
# 
# how to solve this problem?:
# regularization
# data augmentation
# changing the nn arch

# In[15]:


model1.fit(x_train, y_train, batch_size=64, epochs=10   , validation_data=(x_val, y_val))


# This is the example of using a regularizer to solve the overfitting problem.

# In[ ]:


#Functional API
inputs = keras.Input(shape=(32,32,3))
x = Conv2D(32,3,kernel_regularizer=keras.regularizers.l2(0.01))(inputs) #32 channels of filters and 3x3 kernel(size of filter applied) then can also mention the stride
x = BatchNormalization()(x)# ensure to do batch normalization before adding the relu
x=keras.activations.relu(x)
x=MaxPooling2D(2)(x)


x = Conv2D(64,3,)(inputs) 
x = BatchNormalization()(x)
x=keras.activations.relu(x)
x=MaxPooling2D(2)(x)


x = Conv2D(128,3,)(inputs) 
x = BatchNormalization()(x)
x=keras.activations.relu(x)
x=MaxPooling2D(2)(x)


x=Flatten()(x)

x=Dense(64, activation='relu')(x)
x=keras.layers.Dropout(0.5)(x)
outputs = Dense(10, activation ='softmax')(x)

model2 = keras.Model(inputs =inputs , outputs = outputs)


# In[ ]:


model2.compile(optimizer=keras.optimizers.Adam(3e-4), loss=keras.losses.SparseCategoricalCrossentropy(), metrics=['accuracy'])


# In[ ]:


model2.fit(x_train, y_train, batch_size=64, epochs=10   , validation_data=(x_val, y_val))


# Regularization solves the problem of overfitting by simplyfying the model and dropout some connections.

# for dnn
# 
# class dnn(layers.model)

# Subclassing method for cnn

# In[ ]:


class CNNBlock(layers.Layer):
    def __init__(self, output_channels, kernel_size=3, ):
        super(CNNBlock, self).__init__()
        self.conv = Conv2D(output_channels, kernel_size)
        self.bn = BatchNormalization()
        self.pool = MaxPooling2D(2)# default value is already 2

    def call(self, inputs):
        x = self.conv(inputs)
        x = self.bn(x)
        x = keras.activations.relu(x)
        return self.pool(x)
    


# In[ ]:


model2.Sequential([
    CNNBlock(32),
    CNNBlock(64),
    CNNBlock(128),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])


# In[ ]:


model2.compile(optimizer=keras.optimizers.Adam(3e-4), loss=keras.losses.SparseCategoricalCrossentropy(), metrics=['accuracy'])
model2.fit(x_train, y_train, batch_size=64, epochs=10   , validation_data=(x_val, y_val))


# # __Tranfer Learning and Callbacks__:
# Using pretrained models
# Using Same arch and weights from the pretrained model of a large dataset.
# In our own dataset we can have a differnet input shape and output classes can be different
# 
# 
# 
# # __Fine tuning__
# When the weights of all the layers are retrained along with the layers given. The initial layers are freezed as in they do not get trained. but the output layers are customized to fit a lot better to the current data that may have less number of classes. The weights are learned only for the new model added.

# In[26]:


model.save('path')
pre_trained_model = tf.keras.models.load_model('path')


# In[27]:


(x_train1, y_train1), (x_train2, y_train2) = keras.datasets.cifar100.load_data()


# In[28]:


x_train1.shape


# In[ ]:


pre_trained_model.summary()


# In[ ]:


pre_trained_inputs = pre_trained_model.layers[0].input
pre_trained_outputs = pre_trained_model.layers[-2].output
outputs = Dense(100, activation='softmax')(pre_trained_outputs)
model3 = keras.Model(inputs = pre_trained_inputs, outputs =  outputs)

model3.compile(optimizer=keras.optimizers.Adam(3e-4), loss=keras.losses.SparseCategoricalCrossentropy(), metrics=['accuracy'])
model3.fit(x_train1, y_train1, batch_size=64, epochs=10   , validation_data=(x_train2, y_train2))


# In[ ]:


pre_trained_inputs = pre_trained_model.layers[0].input
pre_trained_outputs = pre_trained_model.layers[-2].output
outputs = Dense(100, activation='softmax')(pre_trained_outputs)
model4 = keras.Model(inputs = pre_trained_inputs, outputs =  outputs)


for layer in pretrained_model.layers[-6:]:
    layer.trainable = True

model3.compile(optimizer=keras.optimizers.Adam(3e-4), loss=keras.losses.SparseCategoricalCrossentropy(), metrics=['accuracy'])
model3.fit(x_train1, y_train1, batch_size=64, epochs=10   , validation_data=(x_train2, y_train2))

