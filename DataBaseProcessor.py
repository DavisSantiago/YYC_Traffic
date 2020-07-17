from pymongo import MongoClient
import pandas as pd

client = MongoClient("mongodb+srv://davis:ENSF592@cluster0.qo5yv.mongodb.net/Cluster0?retryWrites=true&w=majority")


# processing 2016 traffic volume

db = client['YYC_Traffic']
collection = db['TrafficFlow2016']
data = pd.read_csv('TrafficFlow2016_OpenData.csv')

headers = {'secname': 'segment', 'the_geom': 'coordinates', 'year_vol': 'year', 'shape_leng': 'length'}
data.rename(columns=headers, inplace=True)

data_dict = data.to_dict("records")

collection.insert_many(data_dict)


# processing 2017 traffic volume

db = client['YYC_Traffic']
collection = db['TrafficFlow2017']
data = pd.read_csv('2017_Traffic_Volume_Flow.csv')

headers = {'segment_name': 'segment', 'the_geom': 'coordinates', 'length_m': 'length'}
data.rename(columns=headers, inplace=True)

data_dict = data.to_dict("records")

collection.insert_many(data_dict)


# processing 2018 traffic flow

db = client['YYC_Traffic']
collection = db['TrafficFlow2018']
data = pd.read_csv('Traffic_Volumes_for_2018.csv')
print(data.info())
headers = {'YEAR': 'year', 'SECNAME': 'segment', 'Shape_Leng': 'length', 'VOLUME': 'volume', 'multilinestring': 'coordinates'}

data.rename(columns=headers, inplace=True)
print(data.info())
data_dict = data.to_dict("records")

collection.insert_many(data_dict)


# processing 2016 traffic incidents

db = client['YYC_Traffic']
collection = db['TrafficIncidents2016']
data = pd.read_csv('Traffic_Incidents_Archive_2016.csv')

headers = {'INCIDENT INFO': 'address', 'DESCRIPTION': 'description', 'START_DT': 'start_time',
           'MODIFIED_DT': 'modified_time', 'QUADRANT': 'quadrant', 'Longitude': 'longitude', 'Latitude': 'latitude',
           'Count': 'count'}
data.rename(columns=headers, inplace=True)

data.reset_index(inplace=True)
data_dict = data.to_dict("records")

collection.insert_many(data_dict)


# processing 2017 traffic incidents

db = client['YYC_Traffic']
collection = db['TrafficIncidents2017']
data = pd.read_csv('Traffic_Incidents_Archive_2017.csv')

data.rename(columns=headers, inplace=True)

data.reset_index(inplace=True)
data_dict = data.to_dict("records")

collection.insert_many(data_dict)


# processing traffic incidents large file

db = client['YYC_Traffic']
collection = db['TrafficIncidents']
data = pd.read_csv('Traffic_Incidents.csv')

data.rename(columns=headers, inplace=True)

data.reset_index(inplace=True)
data_dict = data.to_dict("records")

collection.insert_many(data_dict)
