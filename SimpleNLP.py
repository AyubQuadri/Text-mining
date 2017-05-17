from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

#simpel Corpora

example_text = "Hello Mr Smith, how are you doing today? what are your plannes for the reset of the day. Shall we have a cup of coffee?"

#1.Tokenizer: Sent Tokenizer and Word Tokenizer 

print(sent_tokenize(example_text))
#print(word_tokenize(example_text))

#Word Tokenizer line by line
#for i in word_tokenize(example_text):
	#print(i)

#2. Stop Words

#check stop words from english corpora
stop_words = set(stopwords.words("english"))
#print(stop_words)

words = word_tokenize(example_text)


#To print the filtered text in a loop 
#filtered_text=[]

# for w in words:
# 	if w not in stop_words:
# 		filtered_text.append(w)   ---->>> filtered_text = [w for w in words if not w in stop_words]


#short hand to print the filtered text removing stop words
filtered_text = [w for w in words if not w in stop_words]
print(filtered_text)