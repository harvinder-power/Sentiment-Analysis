import tweepy
from textblob import TextBlob

#consumer and access key obtained through request at apps.twitter.com
consumer_key = "****"
consumer_secret = "****"

access_token = "****"
access_token_secret = "****" 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

sentiment_search = raw_input('What would you like to know about?')
public_tweets = api.search(sentiment_search)

for tweet in public_tweets:
    print (tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)