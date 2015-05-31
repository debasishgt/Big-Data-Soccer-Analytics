from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import pymongo
import json
from pymongo import MongoClient
import sys
import tweepy
import time
from bson.son import SON
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def mean(numberList):
    if len(numberList) == 0:
        return float('nan')
    floatNums = [float(x) for x in numberList]
    return sum(floatNums) / len(numberList)

def mode(nums):
    corresponding={}
    occurances=[]
    for i in nums:
            count = nums.count(i)
            corresponding.update({i:count})

    for i in corresponding:
            freq=corresponding[i]
            occurances.append(freq)

    maxFreq=max(occurances)

    keys=corresponding.keys()
    values=corresponding.values()

    index_v = values.index(maxFreq)
    global mode
    mode = keys[index_v]
    return mode


def median(numericValues):
  theValues = sorted(numericValues)
  if len(theValues) % 2 == 1:
    return theValues[(len(theValues)+1)/2-1]
  else:
    lower = theValues[len(theValues)/2-1]
    upper = theValues[len(theValues)/2]
    return (float(lower + upper)) / 2  

def _ss(data):
    """Return sum of square deviations of sequence data."""
    c = mean(data)
    ss = sum((x-c)**2 for x in data)
    return ss

def stdev(data):
    n = len(data)
    if n < 2:
        raise ValueError('variance requires at least two data points')
    ss = _ss(data)
    pvar = ss/n # the population variance
    return pvar**0.5


client = MongoClient('mongodb://localhost:27017/')
db = client.soccer_data
c_data = db.data.aggregate([{'$group': {'_id':'$place.country', 'count':{'$sum' : 1}}}])

#temp = c_data['result']
#temp = temp

arr = []
country = []
for p in c_data:
    if p['_id']:
        country.append(p['_id'])
        arr.append(p['count'])
        
#arr.sort(reverse=True)

#new_arr = []
#for i in range(0,10):
#    new_arr.append(arr[i])

#new_country = []
#for index in range(0,10):
#    for p1 in temp:
#        if p1['count'] == new_arr[index]:
#            new_country.append(p1['_id'])

post_data =[]
for post in db.data.find():
    try:
        tweet = post
        post_data.append(tweet)
    except:
        continue

tweets = pd.DataFrame()
tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, post_data)
tweets_by_country = tweets['country'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Countries', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
tweets_by_country[:10].plot(ax=ax, kind='bar', color='blue')
plt.show()


#print "*****----------Country----------*****"

#print "*****----------Arrays----------*****"	
#print new_arr
#print new_country
print "*****----------Total Records----------*****"
print "                  ", db.data.find({}).count()
print "*****---------------------------------*****"
print "\n"
print "*****---------Location Active---------*****"
print "                   ", db.data.find({'place':{'$ne':None}}).count()
print "*****---------------------------------*****"
print "\n" 
print "*****---------------Mean--------------*****"
print "              ", mean(arr)
print "*****---------------------------------*****"
print "\n"
print "*****---------------Mode--------------*****"
print "                     ", mode(arr)
print "*****---------------------------------*****"
print "\n"
print "*****--------------Median-------------*****"
print "                    ", median(arr)
print "*****---------------------------------*****"
print "\n"
print "*****--------------StDev--------------*****"
print "             ", stdev(arr)
print "*****---------------------------------*****"

