import nltk
from nltk import word_tokenize
from nltk.stem.lancaster import LancasterStemmer

text2 = "Mary closed on closing night when she was in the mood to close."

#stemming
st = LancasterStemmer()
stemmedWords = [st.stem(word) for word in word_tokenize(text2)]
print(stemmedWords)

#POS(part-of-speech) tagging
nltk.pos_tag(word_tokenize(text2))