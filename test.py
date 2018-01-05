import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient('mongodb://localhost:27017')

# Get the sampleDB database
db = client.sampleDB
