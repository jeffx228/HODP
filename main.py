# import the libraries needed for text analysis
#  Natural Language Toolkit is a Python set of libraries commonly used for text analysis

import nltk
from nltk.stem import WordNetLemmatizer
import string
import numpy as np
from nltk.corpus import stopwords
from collections import Counter


#cleaning the input
# stop words are words that carry no meaning ("i", "the", "a", etc.)
stop_words = stopwords.words('english')
# since all emails include 'harvard' and 'college', these would also be considered meaningless words 
stop_words.append("harvard")
stop_words.append("university")
stop_words.append("college")

# punctuation characters
exclude = set(string.punctuation)
exclude.remove('-')
lemma = WordNetLemmatizer()

with open('YaleEmails.txt', 'r+', encoding="utf-8") as f:
    line = f.readlines()

# answer contains the compiled list of key words from each email (2-D array structure)
answer = []
temp = []
previous_date = ""
for x in line:

    if ("DEADBEEF" in x.split()) or  ("deadbeef" in x.split()):

        word_count = Counter(temp)
        answer.extend([word_count.most_common(10)])
        temp = []
    else:

        # reduce the email text input into keywords
        stop_free = " ".join([i.lower() for i in x.split() if i.lower() not in stop_words])
        for y in stop_free.split():
            punc_free = "".join(ch for ch in y if ch not in exclude)
            temp.append(punc_free)

# print results
c = 1
for y in answer:
    print(c)
    print(y)
    print("\n")

    c+=1









