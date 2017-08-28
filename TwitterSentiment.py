from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

#consumer key, consumer secret, access token, access secret.
ckey="sEkkGlkKEa6KCVXPjURD3lUMI"
csecret="lXLUO6wKHqz3dUebG44Ccg1mp3veaSisAyMBPjF9taS8vhL5Hc"
atoken="1018445624-xiy7bObFmrbzDcUxLUXrAXjHPja6y5az8vLJZVz"
asecret="mwImE233p3hGmlYZuSFWEpMGlqYs4GDaazV76fD9SkHPC"

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Donald Trumph"])
