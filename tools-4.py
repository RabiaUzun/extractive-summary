import urllib.request as urllib2
from bs4 import BeautifulSoup
import ssl
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation

ssl._create_default_https_context = ssl._create_unverified_context

articleURL = "https://www.washingtonpost.com/news/the-switch/wp/2016/10/18/the-pentagons-massive-new-telescope-is-designed-to-track-space-junk-and-watch-out-for-killer-asteroids/"

page = urllib2.urlopen(articleURL).read().decode('utf8', 'ignore')
soup = BeautifulSoup(page, "lxml")

text = ''.join(map(lambda p: p.text, soup.find_all('article')))

#text.encode('ascii', errors='replace').replace('?', "")

#For a different url - try next;
'''
def getTextWaPo(url):
    page = urllib2.urlopen(url).read().decode('utf8')
    soup = BeautifulSoup(page,"lxml")
    text = ''.join(map(lambda p: p.text, soup.find_all('article')))
    return text.encode('ascii',errors='replace').replace("?","")
'''

