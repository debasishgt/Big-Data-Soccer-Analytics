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
#print(c_data)

#print(c_data.next())
#temp = c_data.next()
#print temp
arr = []
arr2 = []

while c_data.alive:
	temp = c_data.next()
	if temp['_id']:
		arr2.append(temp['_id'])
		arr.append(temp['count'])

f1=open('stats.txt', 'w+')

print arr2		
f1.write(str(arr2))
print
f1.write(" \n")
#Print the # of TOTAL RECORDS
print("*****------------TOTAL RECORDS------------******")
f1.write("*****------------TOTAL RECORDS------------******")
f1.write(" \n")
print " "
f1.write(" ")
print "                      ", db.data.find({}).count()
f1.write(str(db.data.find({}).count()))
f1.write(" \n")
print
f1.write(" ")
print("*****-------------------------------------******")
f1.write("*****-------------------------------------******")
f1.write(" \n")
print " "
f1.write(" ")


#Print the # of LOCATION ACTIVE Records
print("*****------------LOCATION ACTIVE------------******")
f1.write("*****------------LOCATION ACTIVE------------******")
f1.write(" \n")
print " "
f1.write(" ")
print "                      ", db.data.find({'place':{'$ne':None}}).count()
f1.write(str(db.data.find({'place':{'$ne':None}}).count()))
f1.write(" \n")
print
f1.write(" ")
print("*****---------------------------------------******")
f1.write("*****---------------------------------------******")
f1.write(" \n")
print " "
f1.write(" ")

#Print the entire Array		
print " "
f1.write(" ")
print ("*****-----------------------------------Array-------------------------------------------******")
f1.write("*****-----------------------------------Array-------------------------------------------******")
f1.write(" \n")
print " "
f1.write(" ")
print arr
f1.write(str(arr))
f1.write(" \n")
print("*****------------------------------------------------------------------------------------******")
f1.write("*****------------------------------------------------------------------------------------******")
f1.write(" \n")
print " "
f1.write(" ")

#Print the MEAN
print("*****------------MEAN------------******")
f1.write("*****------------MEAN------------******")
f1.write(" \n")
print " "
f1.write(" ")
mean1 = mean(arr)
print "            ",mean1
f1.write(str(mean1))
f1.write(" \n")
print
f1.write(" ")
print("*****----------------------------******")
f1.write("*****----------------------------******")
f1.write(" \n")
print " "
f1.write(" ")

#Print the MEDIAN
print("*****-----------MEDIAN-----------******")
f1.write("*****-----------MEDIAN-----------******")
f1.write(" \n")
print " "
f1.write(" ")
med1 = median(arr)
print "                 ",med1
f1.write(str(median(arr)))
f1.write(" \n")
print
f1.write(" ")
print("*****----------------------------******")
f1.write("*****----------------------------******")
f1.write(" \n")
print " "
f1.write(" ")

#Print the MODE
print("*****------------MODE------------******")
f1.write("*****------------MODE------------******")
f1.write(" \n")
print " "
f1.write(" ")
mode1 = mode(arr)
print  "                 ",mode1
f1.write(str(mode1))
print
f1.write(" ")
print("*****----------------------------******")
f1.write("*****----------------------------******")
f1.write(" \n")
print " "
f1.write(" ")

#Print the STANDARD DEVIATION
print("*****-----STANDARD DEVIATION-----******")
f1.write("*****-----STANDARD DEVIATION-----******")
f1.write(" \n")
print " "
f1.write(" ")
print  "           ",stdev(arr)
f1.write(str(stdev(arr)))
f1.write(" \n")
print
f1.write(" ")
print("*****----------------------------******")
f1.write("*****----------------------------******")
f1.write(" \n")
print " "
f1.write("*****----------------------------******")
f1.write(" \n")
