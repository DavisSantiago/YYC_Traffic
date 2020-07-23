import DatabaseQuery as Db


class ListBuilder:
    """
    Queries the information from the database and saves it in a list
    """

    @staticmethod
    def build_list(data, collection, year=None, sort=False):
        """
        Queries from the database the correct file based on the arguments, iterates through the information
        and saves it to a list
        :param data: type of information, can be volume or incidents
        :type data: str
        :param collection: Name of the file to query in the database
        :type collection: str
        :param year: a specific year from which we want to see the information
        :type year: str
        :param sort: If we want the information sorted, this argument will be True
        :type sort: bool
        :return: returns a list with the information based on arguments
        :rtype: list
        """
        if data == "volume":
            volume_list = []

            results = Db.Query().query(collection)

            # Iterating through each item in the information fetched from database
            for item in results:
                volume_list.append(
                    (item["segment"], item["coordinates"], item["year"], item["length"], item["volume"]))

            if sort:
                temp = volume_list.copy()
                volume_list = sorted(temp, key=lambda x: x[4], reverse=True)

            return volume_list

        elif data == "incidents":
            incidents_list = []

            results = Db.Query().query(collection)

            if sort:
                # If sort is True, only add the address
                for item in results:
                    if year in item["start_time"]:
                        incidents_list.append((item["address"]))

                incident_count = {}

                # Get the count of accidents in each address and add it to a dict
                for address in incidents_list:
                    if address not in incident_count:
                        incident_count[address] = 1
                    else:
                        incident_count[address] += 1

                # Converting the dict to a list
                temp = list(incident_count.items())

                incidents_list = sorted(temp, key=lambda x: x[1], reverse=True)

                return incidents_list

            else:
                for item in results:
                    if year in item["start_time"]:
                        incidents_list.append(
                            (item["address"], item["description"], item["start_time"], item["modified_time"],
                             item["quadrant"], item["longitude"], item["latitude"], item["location"],
                             item["count"], item["id"]))

                return incidents_list
