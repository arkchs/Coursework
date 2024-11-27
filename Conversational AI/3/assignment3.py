#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pip', 'install nltk')


# 

# In[2]:


import nltk
import pandas as pd


# In[3]:


df = pd.read_csv("docs/IMDB_Dataset.csv")
# print(df.head())


# In[4]:


corpus=[]
for i in range(100):
    corpus.append(df["review"].iloc[i])
# print(corpus)


# In[5]:


lower=[]
for i in corpus:
    lower.append(' '.join([word.lower() for word in i.split()]))
# print(lower)


# In[6]:


alpha=[]
for i in lower:
    alpha.append(' '.join([word for word in i.split() if word.isalpha()]))
# alpha


# In[24]:


tokenize=[]
for i in alpha:
    tokenize.append([word for word in i.split()])
# tokenize


# In[8]:


from nltk.corpus import *
stopword=nltk.corpus.stopwords.words('english') #stopword will contain list of all stopwords of english language
no_stop=[]
for i in tokenize:
    no_stop.append([word for word in i if word not in stopword])
# no_stop


# In[9]:


final=[] #will contain final pre-processed documents
from nltk.stem import PorterStemmer
ps=PorterStemmer()
for i in no_stop:
    final.append(' '.join([ps.stem(word) for word in i]))
# final


# # Binary TDM

# In[10]:


from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(binary=True)
X=cv.fit_transform(final) # returns a binary tdm in compressed sparse row format
# print(X)
binary_tdm_inbuilt=pd.DataFrame(X.toarray().T,index=cv.get_feature_names_out(),columns=[f'{i + 1} docs' for i in range(len(final))])
binary_tdm_inbuilt.shape


# In[11]:


doc_count={} #dictionary for each document
for i in range(len(final)):
    word_count={} #dictionary for words for each document
    for word in final[i].split():
        if word not in word_count.keys():
            word_count[word]=1
    doc_count[f"{i+1} doc"]=word_count
# doc_count


# In[12]:


binary_tdm_scratch = pd.DataFrame(doc_count)
binary_tdm_scratch.fillna(0,inplace=True)
binary_tdm_scratch.shape


# # Term Frequency Matrix

# In[13]:


doc_count1={} #dictionary for each document
for i in range(len(final)):
    word_count1={} #dictionary for words for each document
    for word in final[i].split():
        if word not in word_count1.keys():
            word_count1[word]=0
        word_count1[word]+=1
    doc_count1[f"{i+1} doc"]=word_count1
# doc_count1


# In[14]:


#Converting dictionary to term frequency TDM dataframe
tdm_tf_scratch=pd.DataFrame(doc_count1)
tdm_tf_scratch.fillna(0,inplace=True)
tdm_tf_scratch.shape


# In[15]:


from sklearn.feature_extraction.text import CountVectorizer
cv1=CountVectorizer()
Y=cv1.fit_transform(final) # returns a term frequency tdm in compressed sparse row (csr) format 
# print(Y)
tdm_tf_inbuilt=pd.DataFrame(Y.toarray().T,index=cv1.get_feature_names_out(),columns=[f'{i + 1}.txt' for i in range(len(final))])
tdm_tf_inbuilt.shape


# # TDM Length Normalization

# In[16]:


from sklearn.feature_extraction.text import TfidfVectorizer
tf=TfidfVectorizer(use_idf=False,norm='l1')
Z=tf.fit_transform(final)
tdm_len_norm_inbuilt=pd.DataFrame(Z.toarray().T,index=tf.get_feature_names_out(),columns=[f'{i + 1}.txt' for i in range(len(final))])
tdm_len_norm_inbuilt.shape


# In[17]:


tdm_length_norm_scratch=tdm_tf_scratch.iloc[:,:].div(tdm_tf_scratch.sum(axis=0),axis=1)
tdm_length_norm_scratch.shape


# # TF IDF

# In[18]:


import numpy as np
no_of_docs=len(final)
unique_terms=tdm_length_norm_scratch.index #as idf is computed for each unique term of corpus
idf_count={} #to store idf score of each term of corpus
for term in unique_terms:
    idf_count[term]=0 #initializing entry in idf dictionary
    for doc in final:
        if term in doc.split():
            idf_count[term]+=1
    idf_count[term]=np.log10(no_of_docs/idf_count[term])
idf_series = pd.Series(idf_count)
idf = pd.DataFrame(idf_series)
idf.head()


# In[19]:


tf_idf_scratch=tdm_length_norm_scratch*idf.values
tf_idf_scratch.head()


# In[20]:


from sklearn.feature_extraction.text import TfidfVectorizer
tf1=TfidfVectorizer()
U=tf1.fit_transform(final)
tf_idf_inbuilt=pd.DataFrame(U.toarray().T,index=tf1.get_feature_names_out(),columns=[f'{i + 1}.txt' for i in range(len(final))])
tf_idf_inbuilt.head()


# In[21]:


co_occur_matrix=np.dot(binary_tdm_scratch.values,binary_tdm_scratch.values.T)
np.fill_diagonal(co_occur_matrix,0)
co_occur_matrix=pd.DataFrame(co_occur_matrix, index=binary_tdm_scratch.index,
                            columns=binary_tdm_scratch.index)
co_occur_matrix.head()


# In[22]:


term_frequency = pd.DataFrame(binary_tdm_scratch.sum(axis=1))
term_frequency_independent = term_frequency.dot(term_frequency.T)
ppmi_scratch = (co_occur_matrix * len(final)) / (term_frequency_independent)
ppmi_scratch = np.log(ppmi_scratch)
ppmi_scratch = np.maximum(ppmi_scratch, 0)
ppmi_scratch.head()

