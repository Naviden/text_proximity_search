#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk


# In[5]:


nltk.word_tokenize('ASD SFKE_JNK, LKKkjnkKJN fef')


# In[7]:


docs = ["Iran's most powerful military figure was regarded as the strategic mastermind behind its vast ambition in the Middle East and the country's real foreign minister when it came to matters of war and peace.",
        "As commander of elite special forces, he orchestrated covert operations, involving a web of proxy militias, across the region.",
        "He also commanded political influence inside Iran and was regarded as second only to Iran's all-powerful Supreme Leader.",
        "He was widely considered the architect of President Bashar al-Assad's war in Syria, the ongoing conflict in Iraq, the fight against Islamic State, and many battles beyond.",
        "The silver-haired general with a close-cropped beard was a cult hero for his fighters and the face of evil for his foes.",
        "For years, US officials considered killing a cunning adversary who ordered attacks on their forces and taunted them with social media barbs. "]


# In[55]:


def proximity_search(document_raw, t1, t2, n=5, ordered= False):
    sentences_raw = nltk.sent_tokenize(document_raw)
    sentences = [sentence.lower().strip() for sentence in sentences_raw]
    t1_norm = t1.lower().strip()
    t2_norm = t2.lower().strip()
    for sentence in sentences:
        
        sent_tok = nltk.word_tokenize(sentence)
        if t1_norm in sent_tok and t2_norm in sent_tok:
            diff = sent_tok.index(t2_norm) - sent_tok.index(t1_norm)
            if ordered:
                if diff - 1 <= n and diff-1 > 0:
                    print(document_raw)
            else:
                if abs(diff) - 1 <= n:
                    print(document_raw)
    


# In[55]:


def stats(document_raw, t1, t2, n=5, ordered= False):
    sentences_raw = nltk.sent_tokenize(document_raw)
    sentences = [sentence.lower().strip() for sentence in sentences_raw]
    t1_norm = t1.lower().strip()
    t2_norm = t2.lower().strip()
    for sentence in sentences:
        c_t1 = sentence.count(t1_normrm)
        c_t2 = sentence.count(t2_normrm)
        sent_tok = nltk.word_tokenize(sentence)
        if t1_norm in sent_tok and t2_norm in sent_tok:
            diff = sent_tok.index(t2_norm) - sent_tok.index(t1_norm)
            if ordered:
                if diff - 1 <= n and diff-1 > 0:
                    print(document_raw)
            else:
                if abs(diff) - 1 <= n:
                    print(document_raw)
    


# In[ ]:


# how many pair per sentence
# how many good sent per document


# In[56]:


proximity_search(docs[0], 'figure', 'iran', n=5, ordered=False)


# In[57]:


'aa bb vv'.count('ss')


# In[ ]:




