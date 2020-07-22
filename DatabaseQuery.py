from pymongo import MongoClient


class Query:

    @staticmethod
    def query(collections):
        client = MongoClient(
            "mongodb+srv://davis:ENSF592@cluster0.qo5yv.mongodb.net/Cluster0?retryWrites=true&w=majority")
        db = client["YYC_Traffic"]
        pointer = db[collections]
        results = pointer.find({})
        return results
