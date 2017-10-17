
# coding: utf-8

# ## Preprocessing the Tweets
# 
# 
# Before extracting features from our text data it is important to clean it up. To remove the possibility of having sarcastic tweets in which the sarcasm is either in an attached link or in response to another tweet, we simply discard all tweets that have http addresses in them and all tweets that start with the @ symbol. Ideally we would only collect tweets that are written in English. When we collect sarcastic tweets, the requirement that it contains the label #sarcasm makes it very likely that the tweet will be in English. To maximize the number of English tweets when we collect non-sarcastic tweets, we require that the location of the tweet is either San-Francisco or New-York. In addition to these steps, we remove tweets which contain Non-ASCII characters. We then remove all the hashtags, all the friend tags and all mentions of the word sarcasm or sarcastic from the remaining tweets. If after this pruning stage the tweet is at least 3 words long, we add it to our dataset. We add this last requirement in order to remove some noise from the sarcastic dataset since I do not believe that one can be sarcastic with only 2 words. Finally, we remove duplicates.

# In[ ]:


import string, re
import os.path,os


# In[ ]:


import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


# In[ ]:


def prep(text):
    text = text.lower()
    return text+'\n'


# In[ ]:


def cleanify_non_ascii(PATH):
    '''Generates newtweets.txt in the same directory. Filters non-ascii chars. Didn't remove #'''
    strings = []
    #get all tweets in this list 
    printable = set(string.printable)
    
    fout = open(os.path.join(PATH,'newtweets.txt'),'w')
    i = 0
    for each in strings:
        try:
            each = prep(each)
            fout.write(each.encode('utf-8'))
        except: 
            logging.warning('Filtering out non-unicode characters')
            filtered = filter(lambda x: x in printable,each)
            filtered = prep(filtered)
            fout.write(filtered.encode('utf-8'))
        i += 1
    fout.close()


# In[ ]:




