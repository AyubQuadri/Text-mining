#lemmatizing some form of synonim with same meaning singular <- plural
#lemmatizing is better than stemming

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("pythons"))

print(lemmatizer.lemmatize("gals"))
print(lemmatizer.lemmatize("guys"))

print(lemmatizer.lemmatize("better",pos="a")) #better -> good

print(lemmatizer.lemmatize("beautifully",pos="a"))

print(lemmatizer.lemmatize("saw"))
