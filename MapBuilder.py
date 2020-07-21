import folium
import DatabaseQuery as Db

class MapBuilder:

    def __init__(self, collection, data, year=None):
        self.collection = collection
        self.data = data
        self.year = year

    def build_map(self):

        # query the database based on the parameters passed, will be factored out to its own method later
        results = Db.Query().query(self.collection)
        # for item in results:
        #     print(item)

        if self.data == "incidents":
            table_incidents = []

            for item in results:
                # Selects only rows where the column start_time contains the year passed as an argument
                if self.year in item["start_time"]:
                    table_incidents.append((item["address"]))

            # Empty dictionary to count the accidents per intersection
            accident_count = {}
            # Iterating through every address
            for address in table_incidents:
                if address not in accident_count:
                    # I tried to do the .get(address, 0) + 1 but for some reason it didn't work
                    accident_count[address] = 1
                else:
                    accident_count[address] += 1

            # Making the dictionary a list of tuples
            temp = accident_count.items()
            table = list(temp)
            # Sorting by number of accidents
            table_incidents = sorted(table, key=lambda x: x[1], reverse=True)

            max_section = table_incidents[0][0]
            num_accidents = table_incidents[0][1]
            # had to query again for some reason, only way i could get it to work to retrieve the coordinates
            results = Db.Query().query(self.collection)
            location = ''
            for item in results:
                if max_section in item["address"]:
                    location = item["location"]

            location = location.strip('()')
            lat, long = location.split(',')
            lat, long = float(lat), float(long)

            m = folium.Map(location=[lat, long], zoom_start=15)
            folium.Marker(
                location=[lat, long],
                popup="Number of Incidents = " + str(num_accidents),
                icon=folium.Icon(color='red', icon='info-sign')
            ).add_to(m)
            m.save("IncidentMap.html")


if __name__ == '__main__':
    map_test = MapBuilder("TrafficIncidents", data="incidents", year="2016").build_map()


