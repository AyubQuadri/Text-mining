#Named Entity recognistion 

# NE Type and Examples
# ORGANIZATION - Georgia-Pacific Corp., WHO
# PERSON - Eddy Bonte, President Obama
# LOCATION - Murray River, Mount Everest
# DATE - June, 2008-06-29
# TIME - two fifty a m, 1:30 p.m.
# MONEY - 175 million Canadian Dollars, GBP 10.40
# PERCENT - twenty pct, 18.75 %
# FACILITY - Washington Monument, Stonehenge
# GPE - South East Asia, Midlothian

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
exp_text = state_union.raw("2006-GWBush.txt")

exp_2 = "Hello Mr Smith, how are you doing today? what are your plannes for the reset of the day. Shall we have a cup of coffee at Barista Coffee shop?. I am leaving to India at  twothirty a m, 2:30pm from Maxico so pleaase meet me on time."

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)


# method which takes the text and tagges the sentance and then chunk them up and draw a tree with chucked data
def process_content(text):
	print(text)
	tokenized = custom_sent_tokenizer.tokenize(text)

	try:
		for i in tokenized:
			words = nltk.word_tokenize(i)
			tagged = nltk.pos_tag(words)
			print(tagged)

			namedEnt = nltk.ne_chunk(tagged, binary = True) # binary two tages two to same sub tree
			namedEnt.draw()

	except Exception as e:
		print(str(e))


#process_content(exp_text)

process_content(exp_2)

