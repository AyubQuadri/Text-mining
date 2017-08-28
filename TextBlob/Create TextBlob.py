from textblob import TextBlob as tb
from textblob.classifiers import PositiveNaiveBayesClassifier
# 1. Parts of Speech Tagging using TextBlob Package
Sentance = tb("My Name is Shah Ayub Quadri, I am from India Hyderabad, Facinated by Deep Learning, CNN, RNN & NLP . This is my first attempt for using TextBlob Package")
POS= Sentance.tags
print(POS)

#2. Sentiment Analysis
# function -> text.sentiment
# result -> returns named polairty tuple (Polarity, subjectivity)
# Polarity -> range from [-1.0,1.0]
# Subjectivity -> ranges from [0.0,1.0] 
#				  0.0 -> very objective
#				  0.0 -> very subjective
review = tb("The product release was effective, and the over all release was good as well as smooth")
SENT = review.sentiment
print(SENT)

# 3. Classification 
sports_sentences = ['The team dominated the game','They lost the ball','The game was intense','The goalkeeper catched the ball','The other team controlled the ball']

various_sentences = ['The President did not comment','I lost the keys','The Game was Bad','The team won the game','Sara has two kids','The ball went off the court','The show is over']

classifier = PositiveNaiveBayesClassifier(positive_set=sports_sentences, unlabeled_set=various_sentences)

print(classifier.classify("My team lost the game"))
print(classifier.classify("The Game was "))