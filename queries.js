db.data.find().count()
db.data.find({'place':{'$exists':true}}).count()