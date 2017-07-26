# Twitter Streams Sentiment Analysis
A client designed to generall overall sentiment in streamed tweets in the public Twitter domain. This client uses `TextBlob` for sentiment analysis of words.

## Initialisation
The following pre-requisites must be installled: `Tweepy` and `TextBlob`. This can be done through use of the pip client in terminal (MacOS). This is done through the following commands in terminal:

```
>> sudo easy_install pip
>> pip install tweepy
>> pip install textblob
```

Once these are installed, the client can be run.

## Current State
Currently, the client works to calculate an average sentiment of a topic which is decided by the user. This can be changed:

```
twitterStream.filter(track=["TOPIC TO SEARCH"])
```

Once run, the client generates 3 values per tweet. These are: Tweet count, Polarity, and Sum Polarity. The polarity is a numerical estimate as to the positive/negative sentiment behind the tweet, with positive values reflecting positive sentiment and vice versa. The sum polarity is a running average of the sentiment of the tweets streamed thus far.

The client now visualises data as a graph plotting the polarity of each tweet against time extracted.

## Next Steps
- Update graph rather than re-generate graph after every tweet
- Allow for more than one topic to be analysed concurrently
- Generate exported file for analysis
