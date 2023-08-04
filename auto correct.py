#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
from nltk.corpus import words
from nltk.metrics.distance import edit_distance


# In[2]:


nltk.download('words')


# In[3]:


english_words = set(words.words())
def auto_correct(word):
    word = word.lower()  
    if word in english_words:
        return word
    # Find the closest word using edit distance
    min_distance = float('inf')
    closest_word = None

    for w in english_words:
        distance = edit_distance(word, w)
        if distance < min_distance:
            min_distance = distance
            closest_word = w
    return closest_word
while True:
    input_word = input("Enter a word (type 'exit' to stop): ")

    if input_word.lower() == 'exit':
        break
    corrected_word = auto_correct(input_word)
    print("Input Word:", input_word)
    print("Corrected Word:", corrected_word)


# In[ ]:




