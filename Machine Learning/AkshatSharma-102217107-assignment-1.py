#!/usr/bin/env python
# coding: utf-8

# # __Akshat Sharma 102217107__

# In[17]:


import numpy as np
import imageio


# In[18]:


arr = np.array([1, 2, 3, 6, 4, 5])  
print(np.flip(arr))


# In[19]:


array1 = np.array([[1, 2, 3], [2, 4, 5], [1, 2, 3]])
#flattens the multi dimensional array
print(array1.flatten())
#But when you use ravel, the changes you make to the new array will affect the parent array.
arr2 = array1.ravel()
arr2[-1]=12
print(arr2)


# In[20]:


arr1 = np.array([[1, 2], [3, 4]]) 
arr2 = np.array([[0, 2], [3, 4]]) 
comparison = arr1==arr2
print(comparison)#using the == operator we get an array comparing individual elements of the array
print(comparison.all())#checks if all the elements of comparison is false
print(f"Using inbuild function: {np.array_equal(arr1,arr2)}")


# In[21]:


x = np.array([3,3,4,5,1,1,1,1,2,2,2,2,2,100])
 
#argmax finds the max
print(np.bincount(x))
val = np.bincount(x).argmax()
for i in range(np.size(np.bincount(x))):
    if x[i]==val:
        print(f"index: {i}")
        break
print(f"value: {val}")


# In[22]:


gfg = np.matrix([[4, 1, 9],[ 12, 3, 1],[ 4, 5, 6]])
print(np.sum(gfg))
print(gfg.sum(axis=1))#rows
print(gfg.sum(axis=0))#columns


# In[23]:


n_array = np.array([[55, 25, 15],[30, 44, 2],[11, 45, 77]])
#1st using np
print(np.trace(n_array))
#2nd method using a mask
mask= np.eye(n_array.shape[0],dtype=bool)
print(mask)

np.sum(n_array,where=mask)





eigen_val, eigen_vec = np.linalg.eig(n_array)
print(eigen_val)
print(eigen_vec)

det= np.linalg.det(n_array)
inv = np.linalg.inv(n_array)
print(det)
print(inv)


# In[24]:


p = [[1, 2], 
     [2, 3]] 
q = [[4, 5], 
     [6, 7]] 

print(np.multiply(p,q))

print(np.dot(p,q))


print(np.cov(p))
print(np.cov(q))


# In[25]:


x = np.array([[2, 3, 4], [3, 2, 9]])
y = np.array([[1, 5, 0], [5, 10, 3]])

inner_product = np.dot(x, y.T)  # y.T is the transpose of y
print(inner_product)

outer_product = np.outer(x, y)
print(outer_product)

cartesian_product = np.kron(x, y)
print(cartesian_product)


# In[26]:


array = np.array([[1, -2, 3],[-4, 5, -6]]) 
print(np.abs(array))


flattened_array = array.flatten()
print(np.percentile(flattened_array,[25,50,75]))
print(np.percentile(array,[25,50,75],axis=0))
print(np.percentile(array,[25,50,75],axis=1))


# In[27]:


mean_flattened = np.mean(flattened_array)
median_flattened = np.median(flattened_array)
std_flattened = np.std(flattened_array)

print("Mean, median, and standard deviation for flattened array:\n", mean_flattened, median_flattened, std_flattened)

mean_columns = np.mean(array, axis=0)
median_columns = np.median(array, axis=0)
std_columns = np.std(array, axis=0)

print("Mean, median, and standard deviation for columns:\n", mean_columns, median_columns, std_columns)

mean_rows = np.mean(array, axis=1)
median_rows = np.median(array, axis=1)
std_rows = np.std(array, axis=1)
print("Mean, median, and standard deviation for rows:\n", mean_rows, median_rows, std_rows)


# In[28]:


a = np.array([-1.8, -1.6, -0.5, 0.5, 1.6, 1.8, 3.0])

print(np.floor(a))
print(np.ceil(a))
print(np.trunc(a))
print(np.round(a))


# In[29]:


array = np.array([10, 52, 62, 16, 16, 54, 453])
print(np.sort(array))
print(np.argsort(array))
print(np.sort(array)[:4])
print(np.sort(array)[-5:])


# In[30]:


array = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])
print(array[array % 1 == 0])
print(array[array % 1 != 0])


# In[31]:


def image_to_path(path, savedPath):
  img = imageio.imread(path)

  if img.ndim == 3:
    img_type = 'RGB'
  elif img.ndim == 2:
    img_type = 'Grayscale'
  else:
    raise ValueError("Unsupported image format")

  np.savez_compressed(savedPath, img, img_type, shape=img.shape)
  print('Image Saved')

