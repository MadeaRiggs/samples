import pandas as pd
from sklearn import datasets
from sympy import im

dataset=pd.read_csv('final_dataset_basicmlmodel.csv')
print(dataset.head())

'''
#************
for index, tweet in enumerate(dataset["tweet"][10:15]):
    print(index+1,".",tweet)   
#************
'''
#text cleaning
import re

def clean_text(text):
    #filter to allow only alphabets
    text=re.sub(r'[^a-zA-Z\']', ' ', text)
    #removes unicodes(symbols that seem weird)
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    #to ensure uniformity
    text = text.lower()

    print(text)

dataset['clean_text'] = dataset.tweet.apply(lambda x: clean_text(x))

from wordcloud import STOPWORDS
print(STOPWORDS)

def gen_freq(text):
    word_list=[]

    #not working in the whole code**************
    for words in text.split():
        print(word_list.extend(words))
    #**************************
    word_freq = pd.Series(word_list).value_counts()

    word_freq = word_freq.drop(STOPWORDS, errors='ignore')

    print(word_freq)

#Check whether a negation term is present in the text
def any_neg(words):
    for word in words:
        if word in ['n', 'no', 'non', 'not'] or re.search(r"\wn't", word):
            return 1
    else:
        return 0

#Check whether one of the 100 rare words is present in the text
def any_rare(words, rare_100):
    for word in words:
        if word in rare_100:
            return 1
    else:
        return 0

#Check whether prompt words are present
def is_question(words):
    for word in words:
        if word in ['when', 'what', 'how', 'why', 'who']:
            return 1
    else:
        return 0

word_freq = gen_freq(dataset.clean_text.str)

#100 most rare words in the dataset
rare_100 = word_freq[-100:]
#Number of words in a tweet
dataset['word_count'] = dataset.clean_text.str.split().apply(lambda x: len(x))
#Negation present or not
dataset['any_neg'] = dataset.clean_text.str.split().apply(lambda x: any_neg(x))
#Prompt present or not
dataset['is_question'] = dataset.clean_text.str.split().apply(lambda x: is_question(x))
#Any of the most 100 rare words present or not
dataset['any_rare'] = dataset.clean_text.str.split().apply(lambda x: any_rare(x, rare_100))
#Character count of the tweet
dataset['char_count'] = dataset.clean_text.apply(lambda x: len(x))

#Top 10 common words are
gen_freq(dataset.clean_text.str)[:10]
dataset.head()

#splitting dataset into trainset and testset
from sklearn.model_selection import train_test_split

X = dataset[['word_count', 'any_neg', 'any_rare', 'char_count', 'is_question']]
y = dataset.label

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=27)

from sklearn.naive_bayes import GaussianNB

#Initialize GaussianNB classifier
model = GaussianNB()
#Fit the model on the train dataset
model = model.fit(X_train, y_train)
#Make predictions on the test dataset
pred = model.predict(X_test)

from sklearn.metrics import accuracy_score

print("Accuracy:", accuracy_score(y_test, pred)*100, "%")


