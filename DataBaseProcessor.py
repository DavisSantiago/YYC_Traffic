import pymongo
from pymongo import MongoClient
import pandas

client = MongoClient("mongodb+srv://davis:ENSF592@cluster0.qo5yv.mongodb.net/Cluster0?retryWrites=true&w=majority")
db = client['YYC_Traffic']
collection = db['TrafficFlow2017']


