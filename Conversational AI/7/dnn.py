#!/usr/bin/env python
# coding: utf-8

# In[136]:


import numpy as np
import pandas as pd


# In[137]:


# from sklearn.datasets import make_classification
# X,Y = make_classification(n_samples=1000,n_features=5,n_classes=2,random_state=42)

from sklearn.datasets import load_breast_cancer
X,Y = load_breast_cancer(return_X_y=True)


# This is to use k x n

# In[138]:


X=X.T
X.shape


# In[139]:


Y.shape


# In[140]:


Y=Y.reshape(1,-1)
Y.shape


# Inner activation function should be ReLU and not sigmoid as it the problem of vanishing gradient.

# In[141]:


# nn_arch = [
#     {'hidden_units': 5, 'act_fn': 'none'},
#     {'hidden_units': 5, 'act_fn': 'relu'},
#     {'hidden_units': 4, 'act_fn': 'relu'},
#     {'hidden_units': 3, 'act_fn': 'relu'},
#     {'hidden_units': 1, 'act_fn': 'sigmoid'},
# ]

nn_arch=[
    {'hidden_units':30,'act_fn':'none'}, #input layer
    {'hidden_units':5,'act_fn':'relu'},
    {'hidden_units':4,'act_fn':'relu'},
    {'hidden_units':3,'act_fn':'relu'},
    {'hidden_units':1,'act_fn':'sigmoid'}
]


# In[142]:


num_layers = len(nn_arch)


# weights are not initialized as zero as the z values of all the neruons are same and it will remain as 0 (not so important for bias). When using sigmoid the weigth initialization must be low
# 
# 
# ReLU has the problem of exploding gradient

# In[143]:


def initialize_parameters(nn_arch):
    parameters = {}
    for l in range(1, num_layers):
        #making a random array of weights with small values for the hidden layer according to the following size
        parameters['W'+str(l)] = np.random.randn(nn_arch[l]['hidden_units'], nn_arch[l-1]['hidden_units']) * 0.01
        parameters['B'+str(l)] = np.zeros((nn_arch[l]['hidden_units'],1))
    return parameters


# In[144]:


parameters = initialize_parameters(nn_arch=nn_arch)


# In[145]:


parameters['W3'].shape


# In[146]:


def forward_propagation(X,parameters,nn_arch):
    forward_cache = {}
    A_prev=X
    for l in range(1,len(nn_arch)):
        W = parameters['W'+str(l)]
        b = parameters['B'+str(l)]
        act_fn = nn_arch[l]['act_fn']
        Z = np.dot(W,A_prev)+b
        if act_fn == 'relu':
            forward_cache['Z'+str(l)] = Z
            forward_cache['A'+str(l)] = np.maximum(0,Z)
        elif act_fn == 'sigmoid':
            forward_cache['Z'+str(l)] = Z
            forward_cache['A'+str(l)] = 1/(1+np.exp(-Z))
        A_prev=forward_cache['A'+str(l)]
    forward_cache['A0'] = X
    AL = forward_cache['A'+str(l)]
    return AL,forward_cache


# In[147]:


AL, forward_cache = forward_propagation(X,parameters,nn_arch)


# In[150]:


forward_cache['Z1'].shape


# In[151]:


def compute_cost(AL,Y):
    n = Y.shape[1]
    cost = (-1/n)*np.sum((Y*np.log(AL) + (1-Y)*np.log(1-AL))) 
    return cost


# In[152]:


compute_cost(AL,Y)


# In[153]:


def sigmoid_backward(dA_prev, Z):
    S = 1/(1+np.exp(-Z))
    dS = S * (1-S)
    return dA_prev*dS


# In[154]:


def relu_backward(dA_prev,Z):
    dZ = np.array(dA_prev,copy=True)
    dZ[Z<=0]=0
    return dZ


# In[155]:


def backward_propagation(forward_cache,parameters,nn_arch,Y,AL):
    dAL = (AL-Y)/(AL*(1-AL))
    dA_prev = dAL
    gradients = {}
    n=Y.shape[1]
    for l in reversed(range(1,num_layers)):
        act_fn = nn_arch[l]['act_fn']
        W_curr = parameters['W'+str(l)]
        Z_curr = forward_cache['Z'+str(l)]
        A_prev = forward_cache['A'+str(l-1)]
        if act_fn == 'relu':
            dZ = relu_backward(dA_prev,Z_curr)
            gradients['dW'+str(l)] = (1/n)*(np.dot(dZ,A_prev.T))
            gradients['db'+str(l)] = (1/n)*np.sum(dZ,axis=1,keepdims=True)
            dA_prev = np.dot(W_curr.T,dZ)
        elif act_fn == 'sigmoid':
            dZ = sigmoid_backward(dA_prev,Z_curr)
            gradients['dW'+str(l)] = (1/n)*(np.dot(dZ,A_prev.T))
            gradients['db'+str(l)] = (1/n)*np.sum(dZ,axis=1,keepdims=True)
            dA_prev = np.dot(W_curr.T,dZ)
    return gradients


# In[156]:


gradients = backward_propagation(forward_cache,parameters,nn_arch,Y,AL)


# In[157]:


def update_parameters(parameters,gradients,lr):
    for l in range(1,num_layers):
        parameters['W'+str(l)] = parameters['W'+str(l)]-lr*gradients['dW'+str(l)]
        parameters['B'+str(l)] = parameters['B'+str(l)]-lr*gradients['db'+str(l)]
    return parameters


# In[158]:


def training(X,Y,nn_arch,lr,iterations):
    costs=[]
    parameters = initialize_parameters(nn_arch)
    for i in range(iterations):
        AL,forward_cache = forward_propagation(X,parameters,nn_arch)
        cost = compute_cost(AL,Y)
        if(i%100==0):
            costs.append(cost)
            print(f'iteration {i}: cost: {cost}')
        gradients = backward_propagation(forward_cache,parameters,nn_arch,Y,AL)
        parameters = update_parameters(parameters,gradients,lr)
    return costs,parameters


# In[159]:


costs, parameters = training(X,Y,nn_arch,0.01,10000)


# In[160]:


import matplotlib.pyplot as plt 
plt.plot(costs)

