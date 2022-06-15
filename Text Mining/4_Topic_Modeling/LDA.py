#Step 1: Pre-processing text
#- Tokenize, normalize (lowercase)
#- stop word removal (such as the, is, to, in English)
#- Stemming (normalize the derivation in related forms to the same word)

#Step 2: Convert tokenized documents to a document - term matrix (from identifying which documents have one word to which words are occurring in which documents)

#Step 3: Build LDA models on the doc-term matrix

# doc_set: set of preprocessed text documents
import genism
from genism import corpora, models

dictionary = corpora.Dictionary(doc_set)
corpus = [dictionary.doc2bow(doc) for doc in doc_set] # create the document term matrix
ldamodel = genism.models.ldamodel.LdaModel(corpus, num_topics=4, id2word=dictionary, passes=50)
print(ldamodel.print_topics(num_topics=4, num_words=5)) # We learned 4 topics and looked for the top 5 words of these 4 topics
