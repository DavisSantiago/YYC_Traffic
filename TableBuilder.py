from tkinter import ttk
import ListBuilder as Lb


class TableBuilder:

    def __init__(self, master, results):
        self.results = results
        self.master = master

    def build_table_flow(self, data, year=None, sort=None):
        if data == "incidents":

            if sort == 'sorted':
                table_incidents = Lb.ListBuilder.build_list(data, self.results, year, sort=True)

                tree = ttk.Treeview(master=self.master, column=("Address", "Count"), show='headings')
                tree.heading("Address", text="Address")
                tree.heading("Count", text="Count")

            else:
                table_incidents = Lb.ListBuilder.build_list(data, self.results, year)

                tree = ttk.Treeview(master=self.master, column=("Address", "Description", "Start Time", "Modified Time", "Quadrant",
                                            "Longitude", "Latitude", "Location", "Count", "ID"), show='headings')
                tree.heading("Address", text="Address")
                tree.column("Address", width=150)
                tree.heading("Description", text="Description")
                tree.column("Description", width=100)
                tree.heading("Start Time", text="Start Time")
                tree.column("Start Time", width=100)
                tree.heading("Modified Time", text="Modified Time")
                tree.column("Modified Time", width=100)
                tree.heading("Quadrant", text="Quadrant")
                tree.column("Quadrant", width=40)
                tree.heading("Longitude", text="Longitude")
                tree.column("Longitude", width=100)
                tree.heading("Latitude", text="Latitude")
                tree.column("Latitude", width=100)
                tree.heading("Location", text="Location")
                tree.column("Location", width=100)
                tree.heading("Count", text="Count")
                tree.column("Count", width=25)
                tree.heading("ID", text="ID")
                tree.column("ID", width=30)

            # me messing around and figured out how to change colors of the headers lol
            style = ttk.Style()
            style.configure('Treeview.Heading', font=('Calibri', 13, 'bold'))

            i = 0
            for row in table_incidents:
                tree.insert("", i, values=row)
                i += 1

            return tree

        elif data == "volume":
            if sort:
                table_volume = Lb.ListBuilder.build_list(data, self.results, sort=True)
            else:
                table_volume = Lb.ListBuilder.build_list(data, self.results)

            tree = ttk.Treeview(master=self.master, column=("Segment", "Coordinates", "Year", "Length", "Volume"), show='headings')
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
