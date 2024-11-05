#!/usr/bin/env python
# coding: utf-8

# ### Gautam Garg

# In[32]:


import numpy as np
import imageio


# In[33]:


arr = np.array([1,2,3,6,4,5])
revArray = np.flip(arr)
revArray


# In[34]:


arr = np.array([[1, 2, 3], [2, 4, 5], [1, 2, 3]])
flatten_array = arr.flatten()
flatten_array


# In[35]:


arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[1, 2], [3, 4]])
np.array_equal(arr1, arr2)


# In[36]:


x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])

values, count = np.unique(x, return_counts=True)
mostFreqValue = values[np.argmax(count)]
x_indices =  np.where(x == mostFreqValue)[0]
print(x_indices)

values, count = np.unique(y, return_counts=True)
mostFreqValue = values[np.argmax(count)]
y_indices = np.where(y == mostFreqValue)[0]
print(y_indices)


# In[37]:


gfg = np.matrix('[4,1,9;12,3,1;4,5,6]')
sum = np.sum(gfg)
print(sum)

rowsSum = np.sum(gfg, axis=1)
print(rowsSum)

colSum = np.sum(gfg, axis=0)
print(colSum)


# In[38]:


n_array = np.array([[55, 25, 15],[30, 44, 2],[11, 45, 77]])
print(n_array.trace())

eigenValue, eigenVector = np.linalg.eig(n_array)
print(eigenValue)
print(eigenVector)

revMatrix = np.linalg.inv(n_array)
print(revMatrix)
det = np.linalg.det(n_array)
print(det)


# In[39]:


p = [[1, 2], [2, 3]]
q = [[4, 5], [6, 7]]
r = np.dot(p, q)
r


# In[40]:


p = [[1, 2], [2, 3], [4, 5]]
q = [[4, 5, 1], [6, 7, 2]]
r = np.dot(p, q)
r


# In[41]:


x = np.array([[2, 3, 4], [3, 2, 9]])
y = np.array([[1, 5, 0], [5, 10, 3]])

innerProd = np.inner(x, y)
print(innerProd)

outerProd = np.outer(x, y)
print(outerProd)

cartisianProd = np.cross(x, y)
print(cartisianProd)


# In[42]:


array = np.array([[1, -2, 3],[-4, 5, -6]])
adsValue = np.abs(array)
adsValue


# In[43]:


flattenArray = array.flatten()
percentiles_flattened = np.percentile(flattenArray, [25, 50, 75])
percentiles_columns = np.percentile(array, [25, 50, 75], axis=0)
percentiles_rows = np.percentile(array, [25, 50, 75], axis=1)
print(percentiles_flattened)
print(percentiles_columns)
print(percentiles_rows)

mean_flattened = np.mean(flattenArray)
median_flattened = np.median(flattenArray)
std_flattened = np.std(flattenArray)

mean_columns = np.mean(array, axis=0)
median_columns = np.median(array, axis=0)
std_columns = np.std(array, axis=0)

mean_rows = np.mean(array, axis=1)
median_rows = np.median(array, axis=1)
std_rows = np.std(array, axis=1)

print(mean_flattened)
print(median_flattened)
print(std_flattened)
print(mean_columns)
print(median_columns)
print(std_columns)
print(mean_rows)
print(median_rows)
print(std_rows)


# In[44]:


a = np.array([-1.8, -1.6, -0.5, 0.5,1.6, 1.8, 3.0])
floor = np.floor(a)
ceil = np.ceil(a)
trunc = np.trunc(a)
rounded = np.round(a)
print(floor)
print(ceil)
print(trunc)
print(rounded)


# In[45]:


array = np.array([10, 52, 62, 16, 16, 54, 453])
sortedArray = np.sort(array)
print(sortedArray)

sortedIndices = np.argsort(array)
print(sortedIndices)

smallest_ele = np.sort(array)[:4]
print(smallest_ele)

largest_ele = np.sort(array)[-5:]
print(largest_ele)


# In[46]:


array = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])
intEle = array[array == array.astype(int)]
print(intEle)

floatEle = array[array == array.astype(float)]
print(floatEle)


# In[47]:


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


# In[47]:




