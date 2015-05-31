#!/usr/bin/env python
import pymongo
from textblob import TextBlob    # Sentiment Analysis by Steven Loria & contributors
import re
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from pymongo import MongoClient
import sys
import tweepy
import time
 
# Load utility libs to set encoding and remove urls
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
 
# create connection to your mongodb host - ** REMEMBER TO CHANGE YOUR HOST IP **
client = MongoClient('mongodb://localhost:27017/')

#client = pymongo.MongoClient("192.168.1.xx", 27017)
 
# create db (database variable)
db = client.soccer_data
 
# loop through collection, change text to lower and remove urls
cursor = db.data.find({"text": {"$exists": True}})
output = 0
for item in cursor:
    # tweet preprocessing
	new_tweet = item["text"].lower()                                   # lower
	new_tweet = re.sub(r"(?:\@|https?\://)\S+", "", new_tweet)          # remove urls
 
	sent_tweet = TextBlob(new_tweet)                                    # sentiment
	print
    #print 'Topic: ' + item["topic"]
	print 'Tweet: ' + new_tweet.encode("utf-8")
	print sent_tweet.words
	print sent_tweet.sentences
	print sent_tweet.sentiment
	#print sent_tweet.sentiment.polarity
	output += sent_tweet.sentiment.polarity
	print output
# end