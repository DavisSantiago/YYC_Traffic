from tkinter import ttk


class TableBuilder:

    def __init__(self, results):
        self.results = results

    def build_table_flow(self, data, year=None, sort=None):
        if data == "incidents":
            table_incidents = []

            if sort == 'sorted':

                for item in self.results:
                    # Selects only rows where the column start_time contains the year passed as an argument
                    if year in item["start_time"]:
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

                tree = ttk.Treeview(column=("Address", "Count"), show='headings')
                tree.heading("Address", text="Address")
                tree.heading("Count", text="Count")

            else:
                for item in self.results:
                    if year in item["start_time"]:
                        table_incidents.append(
                            (item["address"], item["description"], item["start_time"], item["modified_time"],
                             item["quadrant"], item["longitude"], item["latitude"], item["location"],
                             item["count"], item["id"]))

                # TODO this is sorting by date just to be able to check that it works, we will need to change it
                if sort == 'sorted':
                    temp = table_incidents.copy()
                    table_incidents = sorted(temp, key=lambda x: x[0], reverse=True)

                tree = ttk.Treeview(column=("Address", "Description", "Start Time", "Modified Time", "Quadrant",
                                            "Longitude", "Latitude", "Location", "Count", "ID"), show='headings')
                tree.heading("Address", text="Address")
                tree.heading("Description", text="Description")
                tree.heading("Start Time", text="Start Time")
                tree.heading("Modified Time", text="Modified Time")
                tree.heading("Quadrant", text="Quadrant")
                tree.heading("Longitude", text="Longitude")
                tree.heading("Latitude", text="Latitude")
                tree.heading("Location", text="Location")
                tree.heading("Count", text="Count")
                tree.heading("ID", text="ID")

            # TODO center data and adjust column size
            # We need to center the data like you did for the other table, but I wasn't sure to which columns to do it
            # We also need to figure out a way to show all the columns in the window

            # me messing around and figured out how to change colors of the headers lol
            style = ttk.Style()
            style.configure('Treeview.Heading', font=('Calibri', 13, 'bold'))

            i = 0
            for row in table_incidents:
                tree.insert("", i, values=row)
                i += 1

            return tree

        elif data == "volume":
            table_volume = []

            for item in self.results:
                table_volume.append(
                    (item["segment"], item["coordinates"], item["year"], item["length"], item["volume"]))

            # If read button clicked it will skip this
            if sort == 'sorted':
                temp = table_volume.copy()
                # Sorting by volume, which is column 4
                table_volume = sorted(temp, key=lambda x: x[4], reverse=True)

            tree = ttk.Treeview(column=("Segment", "Coordinates", "Year", "Length", "Volume"), show='headings')
            tree.heading("Segment", text="Segment")
            tree.heading("Coordinates", text="Coordinates")
            tree.heading("Year", text="Year")
            tree.heading("Length", text="Length")
            tree.heading("Volume", text="Volume")

            # centering the data for these three columns
            tree.column("Year", anchor='n')
            tree.column("Length", anchor='n')
            tree.column("Volume", anchor='n')

            # me messing around and figured out how to change colors of the headers lol
            style = ttk.Style()
            style.configure('Treeview.Heading', font=('Calibri', 13, 'bold'))

            i = 0
            for row in table_volume:
                tree.insert("", i, values=row)
                i += 1

            return tree
