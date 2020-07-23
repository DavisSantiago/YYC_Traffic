from tkinter import ttk
import ListBuilder as Lb


class TableBuilder:
    """
    Builds a table based on the user specified query
    """

    def __init__(self, master):
        self.master = master  # reference to the master of the widget

    def build_table(self, data, collection, year=None, sort=False):
        """
        Builds and returns Treeview Widget (table) containing the results of the user specified query
        :param data: (str) name of the data to be appended (traffic incidents or traffic volume)
        :param collection: (str) the collection name in MongoDB
        :param year: (str) the year of the data
        :param sort: (bool) True if the data should be sorted, False otherwise
        :return: (widget) Treeview widget displaying results
        """

        if data == "incidents":

            # check to see if the data should be sorted
            if sort:
                table_incidents = Lb.ListBuilder.build_list(data, collection, year, sort=True)

                tree = ttk.Treeview(master=self.master, column=("Address", "Count"), show="headings")
                tree.heading("Address", text="Address")
                tree.heading("Count", text="Count")

            else:
                table_incidents = Lb.ListBuilder.build_list(data, collection, year)

                # creating Treeview headings and widget
                tree = ttk.Treeview(master=self.master, column=("Address", "Description", "Start Time", "Modified Time",
                                                                "Quadrant", "Longitude", "Latitude", "Location", "Count",
                                                                "ID"), show="headings")
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

            # setting header styles
            style = ttk.Style()
            style.configure("Treeview.Heading", font=("Calibri", 13, "bold"))

            # append all values from the query to the Treeview table
            i = 0
            for row in table_incidents:
                tree.insert("", i, values=row)
                i += 1

            return tree

        elif data == "volume":
            # check to see if data should be sorted
            if sort:
                table_volume = Lb.ListBuilder.build_list(data, collection, sort=True)
            else:
                table_volume = Lb.ListBuilder.build_list(data, collection)

            # creating Treeview headings and widget
            tree = ttk.Treeview(master=self.master, column=("Segment", "Coordinates", "Year", "Length", "Volume"), show="headings")
            tree.heading("Segment", text="Segment")
            tree.heading("Coordinates", text="Coordinates")
            tree.heading("Year", text="Year")
            tree.heading("Length", text="Length")
            tree.heading("Volume", text="Volume")

            # centering the data for these three columns
            tree.column("Year", anchor="n")
            tree.column("Length", anchor="n")
            tree.column("Volume", anchor="n")

            # setting header styles
            style = ttk.Style()
            style.configure("Treeview.Heading", font=("Calibri", 13, "bold"))

            # append all values from the query to the Treeview table
            i = 0
            for row in table_volume:
                tree.insert("", i, values=row)
                i += 1

            return tree
