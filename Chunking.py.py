import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
exp_text = state_union.raw("2006-GWBush.txt")

exp_2 = "Hello Mr Smith, how are you doing today? what are your plannes for the reset of the day. Shall we have a cup of coffee?"

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

			chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""

			chunkParser = nltk.RegexpParser(chunkGram)
			chunked = chunkParser.parse(tagged)

			print(chunked)

			for subtree in chunked.subtrees(filter= lambda t: t.label() == 'chunk'):
				print(subtree)

			chunked.draw()

	except Exception as e:
		print(str(e))


#process_content(exp_text)

process_content(exp_2)

