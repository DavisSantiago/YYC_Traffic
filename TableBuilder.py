from tkinter import ttk


class TableBuilder:

    def __init__(self, results):
        self.results = results

    def build_table_flow(self, data, year=None, sort=None):

        if data == "incidents":
            table_incidents = []

            for item in self.results:
                if year in item["start_time"]:
                    table_incidents.append((item["address"], item["description"], item["start_time"], item["modified_time"],
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

            # TODO center data

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

            if sort == 'sorted':
                temp = table_volume.copy()
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
