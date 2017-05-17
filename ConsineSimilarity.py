import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer




stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]


print(cosine_sim('What is the step by step guide to invest in share market?', 'What is the step by step guide to invest in share market in india?')) #expected was 0 but got similarity of 0.89
print(cosine_sim('Astrology: I am a Capricorn Sun Cap moon and cap rising...what does that say about me?', 'Im a triple Capricorn (Sun, Moon and ascendant in Capricorn) What does this say about me?'))  #expected was 1 but got similarity of 0.36
print(cosine_sim('I didnt like this movie', 'I really like this movie')) 
print(cosine_sim('My name is Ayub and i love NLP','my name is Ayub and i love NLP'))

