#Part of speech Tagging


# Number # Tag # Description
# 1.		CC	Coordinating conjunction
# 2.		CD	Cardinal number
# 3.		DT	Determiner
# 4.		EX	Existential there
# 5.		FW	Foreign word
# 6.		IN	Preposition or subordinating conjunction
# 7.		JJ	Adjective
# 8.		JJR	Adjective, comparative
# 9.		JJS	Adjective, superlative
# 10.		LS	List item marker
# 11.	MD	Modal
# 12.	NN	Noun, singular or mass
# 13.	NNS	Noun, plural
# 14.	NNP	Proper noun, singular
# 15.	NNPS	Proper noun, plural
# 16.	PDT	Predeterminer
# 17.	POS	Possessive ending
# 18.	PRP	Personal pronoun
# 19.	PRP$	Possessive pronoun
# 20.	RB	Adverb
# 21.	RBR	Adverb, comparative
# 22.	RBS	Adverb, superlative
# 23.	RP	Particle
# 24.	SYM	Symbol
# 25.	TO	to
# 26.	UH	Interjection
# 27.	VB	Verb, base form
# 28.	VBD	Verb, past tense
# 29.	VBG	Verb, gerund or present participle
# 30.	VBN	Verb, past participle
# 31.	VBP	Verb, non-3rd person singular present
# 32.	VBZ	Verb, 3rd person singular present
# 33.	WDT	Wh-determiner
# 34.	WP	Wh-pronoun
# 35.	WP$	Possessive wh-pronoun
# 36.	WRB	Wh-adverb


#Source: Alphabetical list of part-of-speech tags used in the Penn Treebank Project: https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html


import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
exp_text = state_union.raw("2006-GWBush.txt")

exp_2 = "Hello Mr Smith, how are you doing today? what are your plannes for the reset of the day. Shall we have a cup of coffee?"

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)



def process_content(text):
	print(text)
	tokenized = custom_sent_tokenizer.tokenize(text)

	try:
		for i in tokenized:
			words = nltk.word_tokenize(i)
			tagged = nltk.pos_tag(words)
			print(tagged)

	except Exception as e:
		print(str(e))


#process_content(exp_text)

process_content(exp_2)

print(nltk.pos_tag(exp_2))
print(PunktSentenceTokenizer.tokenize(exp_2))