# C:\Users\quadris\AppData\Local\Continuum\Anaconda3\lib\site-packages\nltk\__init__.py 
# inbuild corpora

# 1. loading telugu language corpus
#Loding telugu language
# from nltk.corpus import indian
# from nltk.tokenize import sent_tokenize, word_tokenize

# sample = indian.raw("telugu.pos")

# token = sent_tokenize(sample)

# for i in token:
# 	print(token)


#2. synonyms and antonyms

from nltk.corpus import wordnet

syns = wordnet.synsets("program")

#prints the name of first programme
# print(syns[0].name())

# # prints the name of programme
# print(syns[0].lemmas()[0].name())

# # definiation
# print(syns[0].definition())

# # examples
# print(syns[0].examples())

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
	for l in syn.lemmas():
		synonyms.append(l.name())
		if l.antonyms():
			antonyms.append(l.antonyms()[0].name())


# print(set(synonyms))
# print(set(antonyms))

# Comparing the similarity between ship and boad
w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")

print(w1.wup_similarity(w2))


w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("goat.n.01")

print(w1.wup_similarity(w2))