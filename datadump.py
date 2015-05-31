from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import pymongo
import json
from pymongo import MongoClient
import sys
import tweepy
import time



#insert your API key
consumer_key = 'd8iL5X7d8ioERyrQDeBRrSmgJ'
#insert your API secret
consumer_secret = '7zSzX11yuvNASuOB5HcqEAVSA1wsEf5LmsbnFz2x0eyWrUlxyu'
#insert your access token
access_token = '157268137-kBTrGECsMLD6d8CTjwavFNdhcF5iXDdZNBnT9sah'
#insert your access token secret
access_token_secret = '0OhvXlJcnEotZxH2qKt4gQg0pVxKscWjkr2lUt9cA8Syg'

class StdOutListener(StreamListener):

    def on_data(self, data):


        seq = {'created_at', 'user', 'place', 'text'}
        client = MongoClient('mongodb://localhost:27017/')
 
        # Use cooldb database
        db = client.soccer_data
 
        # Decode JSON
        datajson = json.loads(data)
 
        # We only want to store tweets in Spanish
        #if "lang" in datajson and datajson["lang"] == "es":
            # Store tweet info into the cooltweets collection.
        #if res["Response"] == "True":
        soccerdd = { your_key: datajson[your_key] for your_key in seq }
            
        db.data.insert(soccerdd)

    def on_error(self, status):
        print status




        


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the below keywords
    stream.filter(track=['#FIFA', '#fifa','#FIFAWorldCup','#fifaworldcup','#Brazil2014','#ussoccer','#worldcup'])
