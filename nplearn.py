from textblob import TextBlob


my_sentence=TextBlob("I am reading a blog post on AnalyticsVidhya. I am loving it!")

print(my_sentence.tags) #POS tagging operation
print(my_sentence.noun_phrases) #extracts the nouns in the sentence

'''
#The range of polarity is [-1,1], with -1
#indicating a negative sentiment and 1 indicating a positive sentiment. Negative words are used to change
#the polarity of a sentence.
#The ‘intensity’ is used by TextBlob to calculate subjectivity. The intensity of a word
#influences whether it modifies the next word. Adverbs are used as modifiers in English.
#The polarity score ranges from -1.0 to 1.0 and the subjectivity ranges from 0.0 to 1.0
#where 0.0 is an objective statement and 1 is a subjective statement.
'''
print(my_sentence.sentiment) #sentiments is explained above
print(my_sentence.words) #word tokenization
print(my_sentence.sentences) #sentence tokenization
print(my_sentence.words[4].pluralize()) #finds plural or singular of the word at the specified index

from textblob import Word 

w= Word("radii").lemmatize() #process of aggregating together the derived forms of a word into a single element or item
print(w)

w=Word("went").lemmatize("v") #lemmantization with the POS tag as the parameter. Example "v" means went as a verb
print(w)

w=Word("went").lemmatize()
print(w)

print(Word("blog").definitions) #defines the specified word

word1=Word("phone").synsets #returns a list of synset objects for a particular word.
print(word1)

my_sentence=TextBlob("I am not in danger. I am the dyangr").correct() #does spell check operation
print(my_sentence)

w=Word("neumonia").spellcheck() #returns a list of probably correct words along with the confidence in the form of a tuple.
print(w)

betty = TextBlob("Betty Botter bought some butter. But she said the Butter’s bitter. If I put it in my batter, it will make my batter bitter. But a bit of better butter will make my batter better.").word_counts['butter']
print(betty)

my_sentence=TextBlob("I am reading a blog post on AnalyticsVidhya. I am loving it!")
print(my_sentence.parse()) #process of analyzing strings of symbols in natural language that correspond to formal grammar rules.The “parse()” method parses the TextBlob by including the tags besides the words.

my_sentence=TextBlob("Simple is better than complex.") 
print(my_sentence[0:16]) #slicing operations

print(my_sentence.upper()) #uppercase of the words

print(my_sentence.find("better")) #finds the specified word

a=TextBlob("Black")
b=TextBlob("Blue")
print(a + ' and ' + b) #concatenation

print("{0} and {1}".format(a,b)) #formatting

bob= TextBlob("How many roads should a man must walk before we can call him a man?").ngrams(n=3) #constructing a trigram
print(bob)



