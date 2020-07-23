from pymongo import MongoClient


class Query:
    """
    Queries the database and returns a cursor for the user specified collection
    """

    @staticmethod
    def query(collections):
        """
        Finds the specified collection within the database and returns a cursor with all of the documents
        :param collections: (str) the name of the collection we are going to query
        :return: (cursor) cursor for the specified collection
        """
        # Connecting to MongoDB
        client = MongoClient(
            "mongodb+srv://davis:ENSF592@cluster0.qo5yv.mongodb.net/Cluster0?retryWrites=true&w=majority")
        # The name of our database
        db = client["YYC_Traffic"]
        # Querying to the specified collection within our database
        pointer = db[collections]
        # Retrieving all data
        results = pointer.find({})
        # Returning the cursor
        return results
