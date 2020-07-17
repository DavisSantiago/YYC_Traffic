from pymongo import MongoClient
import tkinter as tk
from tkinter import ttk
import DatabaseQuery as Db
import TableBuilder as Tb

# client = MongoClient("mongodb+srv://davis:ENSF592@cluster0.qo5yv.mongodb.net/Cluster0?retryWrites=true&w=majority")
# db = client['YYC_Traffic']
# collection = db['TrafficFlow2016']
#
# results = collection.find({})

query = Db.Query()
results = query.query()
tree = Tb.TableBuilder(results).build_table_flow()
print(type(tree))

def print_table(index):
    main_table = []

    for item in results:
        main_table.append((item["segment"], item["coordinates"], item["year"], item["length"], item["volume"]))

    if index == "":
        print_gui(main_table)

    if index == "Segment":
        temp = sorted(main_table, key=lambda x: x[0])
        print_gui(temp)

    if index == "Coordinates":
        temp = sorted(main_table, key=lambda x: x[1])
        print_gui(temp)

    if index == "Year":
        temp = sorted(main_table, key=lambda x: x[2])
        print_gui(temp)

    if index == "Length":
        temp = sorted(main_table, key=lambda x: x[3])
        print_gui(temp)

    if index == "Volume":
        temp = sorted(main_table, key=lambda x: x[4], reverse=True)
        print_gui(temp)


def sort_table(index=""):
    print_table(index)


def print_gui(table):
    window = tk.Tk()
    tree = ttk.Treeview(window, column=("Segment", "Coordinates", "Year", "Length", "Volume"), show='headings')
    tree.heading("Segment", text="Segment")
    tree.heading("Coordinates", text="Coordinates")
    tree.heading("Year", text="Year")
    tree.heading("Length", text="Length")
    tree.heading("Volume", text="Volume")
    tree.pack()

    i = 0
    for row in table:
        tree.insert("", i, values=row)
        i += 1

    window.mainloop()


if __name__ == '__main__':
    sort_table()
    # sort_table("Segment")
    # sort_table("Year")
    # sort_table("Length")
    # sort_table("Volume")
