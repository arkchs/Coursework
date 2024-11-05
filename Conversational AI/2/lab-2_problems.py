#!/usr/bin/env python
# coding: utf-8

# In[13]:


# %run ./API_KEYS.ipynb
# print(API_KEY)


# In[14]:


API_KEY ='0dbf0c77b436e04585917a160371c1ad'
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjMjYyMDM3MTNjZmQ2ODYyY2I0ZWQ3MzAyMmEyODkxMiIsIm5iZiI6MTcyNDk0NzUwMi4xOTkxNTMsInN1YiI6IjY2ZDA5NTlkYjFmYWEyYmI1ZGQzZjhmZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.s0g6bGeFAt-7OpBg15I0sw1r74fURBcPLZACMiWomXA"
}


# In[15]:


base_url = 'https://api.themoviedb.org/3'


# In[16]:


import requests
import pandas as pd
url = "https://api.themoviedb.org/3"
query_url = base_url+'/movie/changes?page=1'
response = requests.get(query_url, headers=headers)
print(response.json())


# # __get the id of the different genre's of the movies__

# In[7]:


def get_data(API_KEY,year,genre_id,page_no):
    query_url = base_url + '/discover/movie?api_key='+API_KEY+'&primary_release_year.gte='+str(year)+'&with_genres='+str(genre_id)+'&page='+str(page_no)+'&sort_by=popularity.desc'
    response = requests.get(query_url)
    if response.stats_code!=200:
        return None
    data=response.json()
    return data['results']


# In[16]:


df = pd.DataFrame(columns=['id','title',])
i=0
while(len(df)<300):
    i+=1
    query_result = get_data('d47af631b1c1b09dcca4c7c32b37e685',2023,35,i)
    if query_result==None:
        continue
    for movie in query_result:
        df.loc[len(df)]=[movie['id'],movie['title']]


# In[ ]:


df.to_csv('/c/Users/aksha/Projects/ConvoAI/movie_titles.csv')


# In[ ]:


ids=[]
def get_similar_movie(API_KEY,movie_id,):
    query_url = base_url +'/movie/'+str(movie_id)+'/similar?api_key='+API_KEY
    response = requests.get(query_url)
    if response.stats_code!=200:    
        return None
    data=response.json()
    for movie in data['results']:
        ids.append(movie['id'])
    return ids


# In[17]:


df1= pd.DataFrame(columns=['movie_id', 'similar_movie_id'])
for movie_id in df['movie_id']:
    query_results = get_similar_movie(API_KEY,movie_id)
    if query_results == None:
        continue
    for i in range(min(5, len(query_results))):
        df1.loc(len(df1)) = [movie_id, query_results[:i]]

