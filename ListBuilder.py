import DatabaseQuery as Db

class ListBuilder:

    @staticmethod
    def build_list(data, collection, year=None, sort=False):
        if data == "volume":
            volume_list = []

            results = Db.Query().query(collection)
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
                for item in results:
                    if year in item["start_time"]:
                        incidents_list.append((item["address"]))

                incident_count = {}

                for address in incidents_list:
                    if address not in incident_count:
                        incident_count[address] = 1
                    else:
                        incident_count[address] += 1

                temp = incident_count.items()
                table = list(temp)

                incidents_list = sorted(table, key=lambda x: x[1], reverse=True)

                return incidents_list

            else:
                for item in results:
                    if year in item["start_time"]:
                        incidents_list.append(
                            (item["address"], item["description"], item["start_time"], item["modified_time"],
                             item["quadrant"], item["longitude"], item["latitude"], item["location"],
                             item["count"], item["id"]))

                return incidents_list
