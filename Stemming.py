#Stemming: removal of ing, 

# I was taking a ride in the car
# I was riding in the car

#ride -> riding came from stem ride. Here Meaning does not change just that we drill down to the stem of the word.

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["python","pythoner","pythoning","pythonly"]

exp_2 =["Act","Acting","Acted","enhanced","saw"]

for w in example_words:
	print(ps.stem(w))

for i in exp_2:
	print(ps.stem(i))