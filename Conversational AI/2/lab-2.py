#!/usr/bin/env python
# coding: utf-8

# # __Data Collection Using APIs__

# In[11]:


import requests
import pandas as pd


# In[12]:





# ### Figuring out the id for the genres

# In[13]:


base_url = 'https://api.themoviedb.org/3'


# In[14]:


endpoint = base_url + "/genre/movie/list?api_key="
response = requests.get(endpoint, headers=headers)


# In[15]:


if(response.status_code==200):
    print(response.json())
else:
    print('Something Weng Wrong! '+str(response.status_code))


# In[42]:


def get_movies(pageno):
    endpoint_1 = base_url + "/discover/movie"
    options_1 = f"?include_adult=false&include_video=false&language=en-US&page={pageno}&sort_by=popularity.desc&with_genres=35"
    endpoint_1 = endpoint_1 + options_1
    discover_response = requests.get(endpoint_1,headers=headers)
    if(discover_response.status_code!=200):
        print("Something Went Wrong! "+str(discover_response.status_code))
        return discover_response
    else:
        # print(discover_response.json())
        return discover_response


# ### The output format is uncomprehensible! Let's fix that.

# In[39]:


get_movies(1)


# In[50]:


df = pd.DataFrame(columns=['title','related_genres','genre'])
for page in range(1,16):
        all_movies_response = get_movies(page)
        if all_movies_response.status_code!=200:
              break
        all_comedy_movies = all_movies_response.json()
        movie_info = []
        
        for movie in all_comedy_movies['results']:
            movie_info = []
            title = movie['title']
            movie_info.append(title)
            related_genres = movie['genre_ids']
            genre = movie['id']
            movie_info.append(related_genres)
            movie_info.append(genre)
            # print(movie_info)
            df.loc[len(df)] = movie_info


# In[51]:


df.head()


# In[52]:


df.to_csv('movie_ID_name.csv')

