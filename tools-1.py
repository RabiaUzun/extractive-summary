import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.collocations import *

text = "Mary had a little lamb. Her fleece was white as snow"

# sentence tokenization
sents = sent_tokenize(text)
print(sents)

# word tokenization
words = [word_tokenize(sent) for sent in sents]
print(words)

# removing stopwords
customStopWords = set(stopwords.words('english')+list(punctuation))
wordsWOStopwords = [word for word in word_tokenize(text) if word not in customStopWords]
print(wordsWOStopwords)

# identifying bigrams
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(wordsWOStopwords)
sorted(finder.ngram_fd.items())