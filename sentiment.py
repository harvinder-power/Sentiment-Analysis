import tweepy
from textblob import TextBlob
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from tweepy import Stream

from tweepy.streaming import StreamListener

plotly.tools.set_credentials_file(username='XXXX', api_key='XXXX')


#consumer and access key obtained through request at apps.twitter.com
consumer_key = "XXXX"
consumer_secret = "XXXX"

access_token = "XXXX"
access_token_secret = "XXXX" 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class listener(StreamListener):    
    def __init__(self):
        self.tweet_count = 0
        self.sum_polarity = 0
        
    def on_data(self, data):
        #tweet_count = int()
        #sum_polarity = int()
        
        #print data
        pure_tweet = data.split(',"text":"')[1].split(',"source"')[0]
        print pure_tweet
        
        polarity = TextBlob(pure_tweet).sentiment.polarity
        print "Polarity = ", polarity
        
        #tweet_count += 1
        print "tweet count = ", self.tweet_count
        self.tweet_count = self.tweet_count + 1

        #sum_polarity += polarity
        print "sum polarity = ", self.sum_polarity
        self.sum_polarity = self.sum_polarity + polarity 
    
        #if tweet_count > 0:
        avg_polarity = self.sum_polarity/self.tweet_count
        print "Average Polarity =", avg_polarity
        
        return True
    
    def on_error(self, data):
        print status
        

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["brexit"])