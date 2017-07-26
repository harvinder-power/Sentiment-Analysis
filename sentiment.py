import tweepy
from textblob import TextBlob
from tweepy import Stream
import numpy as np
import matplotlib.pyplot as plt
from tweepy.streaming import StreamListener
from datetime import datetime

consumer_key = "XXX"
consumer_secret = "XXX"

access_token = "XXX"
access_token_secret = "XXX" 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class listener(StreamListener):    
    def __init__(self):
        self.tweet_count = 0
        self.sum_polarity = 0
        self.all_data = []
        self.time_stamps = []
        
    def on_data(self, data):
        #tweet_count = int()
        #sum_polarity = int()
        
        #print tweet data
        pure_tweet = data.split(',"text":"')[1].split(',"source"')[0]
        print pure_tweet
        
        #print polarity of tweet
        polarity = TextBlob(pure_tweet).sentiment.polarity
        print "Polarity = ", polarity
        
        #tweet_count += 1
        print "tweet count = ", self.tweet_count
        self.tweet_count = self.tweet_count + 1

        #sum_polarity += polarity
        print "sum polarity = ", self.sum_polarity
        self.sum_polarity = self.sum_polarity + polarity 
    
        #calculate and print average polarity for tweets so far
        avg_polarity = self.sum_polarity/self.tweet_count
        print "Average Polarity =", avg_polarity
    
        #creating a list of all polarity values
        self.all_data.append(avg_polarity)
        #print "All data list = ", self.all_data
        
        #generating time stamps for extraction times (though this should be the time of time ideally)
        self.time_stamps.append(datetime.now())
        #print "Time stamps = ", self.time_stamps
        
        #plotting the graph
        plt.plot(self.time_stamps, self.all_data, 'ro')
        plt.xlabel('Time')
        plt.ylabel('Polarity of Sentiment')
        plt.title('Sentiment of tweets against time')
        plt.draw()
        #if self.tweet_count % 10 == 0:
        plt.show()
        
    def on_error(self, data):
        print status
        

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["brexit"])