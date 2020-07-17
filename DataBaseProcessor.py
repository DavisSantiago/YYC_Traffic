import pymongo
from pymongo import MongoClient
import pandas as pd

client = MongoClient("mongodb+srv://davis:ENSF592@cluster0.qo5yv.mongodb.net/Cluster0?retryWrites=true&w=majority")
db = client['YYC_Traffic']
collection = db['TrafficFlow2017']

data = pd.read_csv('2017_Traffic_Volume_Flow.csv')



# data.reset_index(inplace=True)
# data_dict = data.to_dict("records")
#
# collection.insert_many(data_dict)
import pymongo
from pymongo import MongoClient
import pandas

client = MongoClient("mongodb+srv://davis:ENSF592@cluster0.qo5yv.mongodb.net/Cluster0?retryWrites=true&w=majority")
db = client['YYC_Traffic']
collection = db['TrafficFlow2017']


