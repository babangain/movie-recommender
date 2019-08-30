#!/usr/bin/env python
# coding: utf-8

# In[7]:


from gensim.models.doc2vec import Doc2Vec
from sys import argv
model = Doc2Vec.load("doc2vec_Movie_recommender_vec_150_window_10_mc_2_epochs_50.model")
if len(argv) >= 2:
    query = argv[1]
if len(argv) == 3:
    N = int(argv[2])
lst = []
try:
    lst = model.docvecs.most_similar(query,topn=N)
    for i in range(N):
    	print(lst[i][0])
except:
    print("Some Error Occured!!! Please enter movie name correctly and ensure they name is exactly same as in the database")


# In[ ]:




