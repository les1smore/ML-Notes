# WorldNet easily imported into Python through NLTK
import nltk
from nltk.corpus import wordnet as wn

# Find appropriate sense of the words
deer = wn.synset('deer.n.01')
elk = wn.synset('elk.n.01')

# Find path similarity
deer.path_similarity(elk) # result: 0.5
elk.path_similarity(horse) # result: 0.14

# Use an information criteria to find Lin similarity
from nltk.corpus import wordnet_ic
brown_ic = wordnet_ic.ic('ic-brown.dat')

deer.lin_similarity(elk, brown_ic) # result: 0.77
deer.lin_similarity(horse, brown_ic) # result: 0.86

# Use NLTK Collocations and Association measures
import nltk
from nltk.collocations import *

bigram_measures = nltk.collocations.BigramAssocMeasures()

finder = BigramCollocationFinder.from_words(text)
finder.nbest(bigram_measures.pmi, 10) # get the top 10 pairs using the PMI measure from bigram_measures

# finder also has other useful functions, such as frequency filter
finder.apply_freq_filter(10) # restrict any pair not occurring at least 10 times in your corpus
