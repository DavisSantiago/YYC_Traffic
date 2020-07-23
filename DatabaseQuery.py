from pymongo import MongoClient

class Query:
    """
    Queries from the database and returns a pointer to the data from the collection in the database
    """

    @staticmethod
    def query(collections):
        """
        Finds the specified collection within the database and returns a pointer to its information
        :param collections: (str) the name of the collection we are going to query
        :return: (pointer) pointer to the information of the specified collection
        """
        # The mongodb server URL
        client = MongoClient(
            "mongodb+srv://davis:ENSF592@cluster0.qo5yv.mongodb.net/Cluster0?retryWrites=true&w=majority")
        # The name of our database
        db = client["YYC_Traffic"]
        # Querying to the specified collection within our database
        pointer = db[collections]
        # Retrieving all data
        results = pointer.find({})
        # Returning a pointer to the data
        return results
