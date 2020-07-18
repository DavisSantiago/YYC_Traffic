from tkinter import ttk


class TableBuilder:

    def __init__(self, results):
        self.results = results

    def build_table_flow(self):
        table = []

        for item in self.results:
            table.append((item["segment"], item["coordinates"], item["year"], item["length"], item["volume"]))

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
        for row in table:
            tree.insert("", i, values=row)
            i += 1

        return tree
