from nltk import word_tokenize
from nltk.corpus import wordnet as wn
from nltk.wsd import lesk

# word meaning
for ss in wn.synsets('bass'):
    print(ss, ss.definition())

# WSD(word sense disambiguation)
sense1 = lesk(word_tokenize("Sing in a lower tone, along with the bass"), 'bass')
print(sense1, sense1.definition())

sense2 = lesk(word_tokenize("This sea bass was really hard to catch"), 'bass')
print(sense2, sense2.definition())
