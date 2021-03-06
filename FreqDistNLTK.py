# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 00:37:34 2017

@author: quadris
"""

import nltk
import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), category)
              for category in movie_reviews.categories()
              for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)
print(documents[1])
len(documents)

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
print(all_words.most_common(25))    

print(all_words["stupid"])
