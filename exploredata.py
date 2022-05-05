import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from tensorboard import errors

from wordcloud import WordCloud

dataset=pd.read_csv('tweets.csv', encoding='ISO-8859-1')
print(dataset.head)

def gen_freq(text):
        word_list=[] #stores the list of words

        for tw_words in text.split(): #Loop over all the tweets and extract words into word_list
            word_list.extend(tw_words)
            word_freq=pd.Series(word_list).value_counts() #Create word frequencies using word_list
            word_freq[:20]
     #Print top 20 words
        print(word_freq)

        wc=WordCloud(width=400, height=330, max_words=100, background_color='white').generate_from_frequencies(word_freq)

        plt.figure(figsize=(12, 8))
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.show()

gen_freq(dataset.text.str)


import re
def clean_text(text):
    #Remove RT
    text = re.sub(r'RT', '', text)
    
    #Fix &
    text = re.sub(r'&amp;', '&', text)
    
    #Remove punctuations
    text = re.sub(r'[?!.;:,#@-]', '', text)

    #Convert to lowercase to maintain consistency
    text = text.lower()
    print(text)

#import list of stopwords
from wordcloud import STOPWORDS

print(STOPWORDS)

text= dataset.text.apply(lambda x: clean_text(x))
word_freq=gen_freq(text.str)*100
word_freq=word_freq.drop(labels=STOPWORDS, errors='ignore')
wc = WordCloud(width=450, height=330, max_words=200, background_color='white').generate_from_frequencies(word_freq)

plt.figure(figsize=(12, 14))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()




