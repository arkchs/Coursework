#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pip', 'install nltk')


# In[2]:


import nltk


# In[3]:


nltk.download('stopwords')
nltk.download('brown')
nltk.download('gutenberg')


# In[4]:


from nltk.corpus import gutenberg


# In[5]:


gutenberg.fileids()


# In[6]:


gutenberg.raw(fileids=["austen-emma.txt"])


# In[7]:


gutenberg.words(fileids=['austen-emma.txt'])[:10]


# In[8]:


nltk.download('punkt')


# In[9]:


gutenberg.sents(fileids=['austen-emma.txt'])[:10]


# In[ ]:


gutenberg.raw()


# In[4]:


from nltk.corpus import brown


# In[5]:


brown.categories()


# In[6]:


brown.fileids(categories='humor')


# In[7]:


from nltk.corpus import stopwords


# In[ ]:


stopwords.fileids()#wordnet is a dictionary that is a lexical resource


# In[ ]:


stopwords.words(fileids='hinglish')


# # __Using Custom Corpus__

# In[10]:


path = 'C:/Users/aksha/Projects/Coursework/Conversational AI/3/ConvoDocuments/'
from nltk.corpus import PlaintextCorpusReader
dataset = PlaintextCorpusReader(path,'.*')


# In[11]:


filenames = dataset.fileids()


# In[12]:


corpus=[]
for i in range(len(filenames)):
    corpus.append(dataset.raw(fileids=filenames[i]))


# In[13]:


print(corpus)


# In[14]:


import pandas as pd
df = pd.DataFrame(columns=['text'])
for i in range(len(filenames)):
    df.loc[i] = dataset.raw(fileids=filenames[i])
df


# In[15]:


import os 
filenames1 = os.listdir(path)
print(filenames1)


# In[16]:


corpus1 = []
for i in range(len(filenames1)):
    # print(path+filenames[i])
    f = open(path+filenames1[i])
    corpus1.append(f.read())
    f.close()
print(corpus1)


# In[17]:


norm_token=[]
for doc in corpus:
    norm_token.append([word.lower() for word in doc.split() if word.isalpha()])
print(norm_token)

#need to solve using regexes


# In[18]:


stopwords_list = stopwords.words(fileids='english')


# In[32]:


no_stop=[]
for doc in norm_token:
    no_stop.append([word for word in doc if word not in stopwords_list])
no_stop


# # __Questions__
# ### __M represents a measure of words [V][CV]^m[C]__
# m>0
# 
# Stemmer is pretty bad but still used cause' 
# 1. Semantic meaning is not imp
# 2. Used in Information Retreival
# 

# In[42]:


from nltk.stem import PorterStemmer
ps = PorterStemmer()
finale=[]
for doc in no_stop:
    finale.append(' '.join([ps.stem(word) for word in doc]))
finale


# In[34]:


from nltk.stem import LancasterStemmer
ls = LancasterStemmer()
final1=[]
for doc in no_stop:
    final1.append([ls.stem(word) for word in doc])
final1


# In[35]:


from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()
final2=[]
for doc in no_stop:
    final2.append([wnl.lemmatize(word) for word in doc])
final2


# In[23]:


doc_count = {}
for i in range(len(finale)):
    word_count  = {}
    for word in finale[i].split():
        if word not in word_count.keys():
            word_count[word]=1
    doc_count[filenames[i]]=word_count


# In[24]:


doc_count


# In[25]:


tdm_binary_scratch = pd.DataFrame(doc_count)


# In[26]:


tdm_binary_scratch.fillna(0,inplace=True)


# bigram is used for having two words together as a token

# binary tdm using count vectorizer

# In[37]:


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(binary=True)
X = cv.fit_transform(corpus)


# fit realizes all the parameteres and transform just converts the values in the feature sets 

# In[38]:


cv.get_feature_names_out()


# In[39]:


pd.DataFrame(X.toarray().transpose(),index=cv.get_feature_names_out(), columns=filenames)


# # Term Frequency- Scratch

# In[44]:


doc_count1={}
for i in range(len(finale)):
    word_count1={}
    for word in finale[i].split():
        if word not in  word_count1.keys():
            word_count1[word]=0
        word_count1[word]+=1
    doc_count1[filenames[i]]=word_count1


# In[45]:


doc_count1


# In[48]:


tdm_df_scratch = pd.DataFrame(doc_count1)
tdm_df_scratch.fillna(0, inplace=True)
print(tdm_df_scratch)


# # Term Frequency- Inbuilt

# In[51]:


from sklearn.feature_extraction.text import CountVectorizer
cv1 = CountVectorizer()
X1 = cv1.fit_transform(finale)


# In[56]:


cv1.get_feature_names_out()

tdm_df_inbuilt = pd.DataFrame(X1.toarray().T, index=cv1.get_feature_names_out(),columns=filenames)
tdm_df_inbuilt


# ### Mostly used for normalization of values
# #### length normalization
# #### divide each value by the length of the document

# In[61]:


tdm_len_norm_scratch = tdm_df_scratch.div(tdm_df_scratch.sum(axis=0), axis=1)


# In[63]:


tdm_max_norm_scratch = tdm_df_scratch.div(tdm_df_scratch.max(axis=0), axis=1)
print(tdm_max_norm_scratch)


# In[66]:


import numpy as np

tdm_log_norm_scratch = np.log10(1+tdm_df_scratch)
tdm_log_norm_scratch


# In[72]:


from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(use_idf=False, norm= 'l1')
Y = tfidf.fit_transform(finale)

tdm_len_inbuilt = pd.DataFrame(Y.toarray().T,index=tfidf.get_feature_names_out(), columns=filenames)
print(tdm_len_inbuilt)


# In[75]:


finale


# # Term Frequency IDF

# In[81]:


idf_count = {}
no_of_docs = len(finale)

unique_terms = tdm_df_scratch.index
for term in unique_terms:
    idf_count[term]=0
    for doc in finale:
        if term in doc.split():
            idf_count[term]+=1
    idf_count[term]=np.log10(no_of_docs/idf_count[term])
idf_count


# In[85]:


idf = pd.DataFrame(pd.Series(idf_count), columns=['idfScore'])
idf


# In[90]:


tfidf_scratch = tdm_df_scratch*idf.values
print(tfidf_scratch)


# In[93]:


from sklearn.feature_extraction.text import TfidfVectorizer
tfidf1 = TfidfVectorizer()
Y1 = tfidf1.fit_transform(finale)

tdm_len_inbuilt1 = pd.DataFrame(Y.toarray().T,index=tfidf1.get_feature_names_out(), columns=filenames)
print(tdm_len_inbuilt1)


# there is a difference between sklearn implementation and what we do by scratch. When we add a custom vocabulary we may have the denom in idf to be zero

# # Term Term Matrix

# term term matrix = binary tdm*binary tdm transpose

# In[98]:


co_occ_matrix = np.dot(tdm_binary_scratch.values, tdm_binary_scratch.values.T)
np.fill_diagonal(co_occ_matrix,0)
print(co_occ_matrix)
co_occur_df = pd.DataFrame(co_occ_matrix,index=tdm_binary_scratch.index,columns=)


# In[ ]:




