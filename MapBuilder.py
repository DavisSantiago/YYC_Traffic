import folium
import string
import DatabaseQuery as Db
import ListBuilder as Lb


class MapBuilder:

    def __init__(self, collection, data, year=None):
        self.collection = collection
        self.data = data
        self.year = year

    def build_map(self):

        if self.data == "incidents":
            table_incidents = Lb.ListBuilder.build_list(self.data, self.collection, self.year, sort=True)

            max_section = table_incidents[0][0]
            num_accidents = table_incidents[0][1]

            # had to query again for some reason, only way i could get it to work to retrieve the coordinates
            results = Db.Query().query(self.collection)
            location = ''

            for item in results:
                if max_section in item["address"]:
                    location = item["location"]
                    break

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

        elif self.data == "volume":
            table_volume = Lb.ListBuilder.build_list(self.data, self.collection, self.year, sort=True)

            # extracting the coordinates
            raw_string = table_volume[0][1]
            # formatting the string

            strip_chars = string.ascii_uppercase + ")"
            raw_string = raw_string.strip(strip_chars)
            raw_string = raw_string.replace("(", "")
            coord_list = raw_string.split(",")

            # creating a list of tuples with all coordinates
            lat_long_list = []
            for coordinate in coord_list:
                long, lat = coordinate.split()
                lat_long_list.append((float(lat), float(long)))

            # plotting the map
            m = folium.Map(location=[lat_long_list[0][0], lat_long_list[0][1]], zoom_start=14)
            folium.PolyLine(lat_long_list, weight=8).add_to(m)
            folium.Marker(lat_long_list[0], popup=table_volume[0][0] + " Volume = " + str(table_volume[0][4])).add_to(m)
            m.save("VolumeMap.html")
