import urllib.request as urllib2

import nltk
from bs4 import BeautifulSoup
import ssl
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.collocations import *
from nltk.stem.lancaster import LancasterStemmer
from nltk.probability import FreqDist

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.theguardian.com/science/2020/apr/26/what-if-covid-19-isnt-our-biggest-threat"


def pulltextfromurl(url):
    page = urllib2.urlopen(url).read().decode('utf8')
    soup = BeautifulSoup(page, "lxml")
    text = ''.join(map(lambda p: p.text, soup.find_all('article')))
    return text.encode('ascii', errors='replace').replace("?", "")


article = pulltextfromurl(url)

# sentence tokenization
sents = sent_tokenize(article)

# word tokenization
words = [word_tokenize(sent) for sent in sents]

# removing stopwords
customStopWords = set(stopwords.words('english')+list(punctuation))
wordsWOStopwords = [word for word in word_tokenize(article) if word not in customStopWords]

# identifying bigrams
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(wordsWOStopwords)
sorted(finder.ngram_fd.items())

# stemming
st = LancasterStemmer()
stemmedWords = [st.stem(word) for word in word_tokenize(article)]
print(stemmedWords)

# POS(part-of-speech) tagging
nltk.pos_tag(word_tokenize(article))

# identifying frequency
freq = FreqDist()