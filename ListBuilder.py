import DatabaseQuery as Db


class ListBuilder:
    """
    Queries the database and generates a 2 dimensional list containing the user specified data
    """

    @staticmethod
    def build_list(data, collection, year=None, sort=False):
        """
        Queries the database and generates a 2 dimensional list containing the user specified data
        :param data: (str) name of the data to be appended (traffic incidents or traffic volume)
        :param collection: (str) the collection name in MongoDB
        :param year: (str) the year of the data
        :param sort: (bool) True if the data should be sorted, False otherwise
        :return:
        """

        if data == "volume":
            volume_list = []

            # query the database for the entire collection of data
            results = Db.Query().query(collection)

            # append each parameter to volume_list
            for item in results:
                volume_list.append(
                    (item["segment"], item["coordinates"], item["year"], item["length"], item["volume"]))

            # check if the data should be sorted, if True, sort based on Traffic Volume in ascending order
            if sort:
                temp = volume_list.copy()
                volume_list = sorted(temp, key=lambda x: x[4], reverse=True)

            return volume_list

        elif data == "incidents":
            incidents_list = []

            # query the database for the entire collection of data
            results = Db.Query().query(collection)

            # check if the data should be sorted, if True, sort based on number of incidents at that address
            if sort:
                # iterate through the query and append addresses that match the user specified year
                for item in results:
                    if year in item["start_time"]:
                        incidents_list.append((item["address"]))

                incident_count = {}

                # determine how many incidents occur at the same address by using a dictionary
                for address in incidents_list:
                    if address not in incident_count:
                        incident_count[address] = 1
                    else:
                        incident_count[address] += 1

                # convert the dictionary to a list
                temp = incident_count.items()
                table = list(temp)

                # sort the list based on the number of accidents in ascending order
                incidents_list = sorted(table, key=lambda x: x[1], reverse=True)

                return incidents_list

            else:
                # iterate through the query and append all data that matches the user specified year
                for item in results:
                    if year in item["start_time"]:
                        incidents_list.append(
                            (item["address"], item["description"], item["start_time"], item["modified_time"],
                             item["quadrant"], item["longitude"], item["latitude"], item["location"],
                             item["count"], item["id"]))

                return incidents_list
