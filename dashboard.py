import pymongo
import json
from pymongo import MongoClient
import sys
import tweepy
import time
from bson.son import SON




client = MongoClient('mongodb://localhost:27017/')
db = client.soccer_data
c_data = db.data.aggregate([{'$group': {'_id':'$place.country', 'count':{'$sum' : 1}}}])

#temp = c_data['result']

NA = 0
SA = 0
AS = 0
EU = 0
AF = 0
AU = 0

country = []
for p in c_data:
    if p['_id']:
		if p['_id'] == 'United States':
			print "2.."
			NA = NA + p['count']
		elif p['_id'] == 'Brasil':
			print "3.."
			SA = SA + p['count']
		elif p['_id'] == 'United Kingdom':
			print "4.."
			EU = EU + p['count']
		elif p['_id'] == 'Argentina':
			print "5.."
			SA = SA + p['count']
		elif p['_id'] == 'Indonesia':
			print "6.."
			AS = AS + p['count']
		elif p['_id'] == 'France':
			print "7.."
			EU = EU + p['count']
		elif p['_id'][:4] == 'Espa':
			print "8.."
			EU = EU + p['count']
		elif p['_id'] == 'Nederland':
			print "9.."
			EU = EU + p['count']
		elif p['_id'] == 'Chile':
			print "10.."
			SA = SA + p['count']
		elif p['_id'] == 'Uruguay':
			print "11.."
			SA = SA + p['count']
		#elif p['_id'][-4:] == 'xico':
		elif p['_id'] == 'South Africa':
			print "12.."
			AF = AF + p['count']

jsonData = [
{"id": "NA", "value": str(NA)}, 
{"id": "SA", "value": str(SA)}, 
{"id": "AS", "value": str(AS)}, 
{"id": "EU", "value": str(EU)}, 
{"id": "AF", "value": str(AF)}, 
{"id": "AU", "value": str(AU)}
]
with open('jsonData.json', 'w') as outfile:
    json.dump(jsonData, outfile)
		
print "NA", NA
print "AU", AU
print "AF", AF
print "EU", EU
print "AS", AS
print "SA", SA
