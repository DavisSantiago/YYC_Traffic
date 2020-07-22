import tkinter as tk
from tkinter import ttk
import GraphBuilder as Gb
import MapBuilder as Mb
import TableBuilder as Tb
from pymongo.errors import OperationFailure


class LeftFrame(tk.Frame):

    def __init__(self, master, root):
        tk.Frame.__init__(self, master)
        self.root = root
        self.display = tk.Frame()  # temp frame so that we can use .destroy right before calling the new updated frame
        self.build_frame()

    def build_frame(self):
        # Event listener for read button
        def read_cmd():
            if type_combo.get() == "Traffic Volume":
                if year_combo.get() == "2016":
                    # Clears the previous message
                    # Builds frame, no filter means the data will be displayed as it is on the file
                    # Because this button is for read only, all the method calls will have this no filter
                    self.display.destroy()
                    try:
                        self.display = Tb.TableBuilder(self.root).build_table_flow("volume", "TrafficFlow2016", "2016")
                        self.display.pack(fill="both", side="right", expand=True)
                        status_msg.set("Successfully read\nfrom Database")
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating table")
                elif year_combo.get() == "2017":
                    self.display.destroy()
                    try:
                        self.display = Tb.TableBuilder(self.root).build_table_flow("volume", "TrafficFlow2017", "2017")
                        self.display.pack(fill="both", expand=True)
                        status_msg.set("Successfully read\nfrom Database")
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating table")
                elif year_combo.get() == "2018":
                    self.display.destroy()
                    try:
                        self.display = Tb.TableBuilder(self.root).build_table_flow("volume", "TrafficFlow2018", "2018")
                        self.display.pack(fill="both", expand=True)
                        status_msg.set("Successfully read\nfrom Database")
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating table")
                # If there is no year selected
                else:
                    status_msg.set("Please select a Year")

            elif type_combo.get() == "Traffic Accidents":
                if year_combo.get() == "2016":
                    # I pulled all the data from the same file, we can delete the other ones from out database
                    # The added argument filters, from the file, only data that happened in that year
                    self.display.destroy()
                    try:
                        self.display = Tb.TableBuilder(self.root).build_table_flow("incidents", "TrafficIncidents", "2016")
                        self.display.pack(fill="both", expand=True)
                        status_msg.set("Successfully read\nfrom Database")
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating table")
                elif year_combo.get() == "2017":
                    self.display.destroy()
                    try:
                        self.display = Tb.TableBuilder(self.root).build_table_flow("incidents", "TrafficIncidents", "2017")
                        self.display.pack(fill="both", expand=True)
                        status_msg.set("Successfully read\nfrom Database")
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating table")
                elif year_combo.get() == "2018":
                    self.display.destroy()
                    try:
                        self.display = Tb.TableBuilder(self.root).build_table_flow("incidents", "TrafficIncidents", "2018")
                        self.display.pack(fill="both", expand=True)
                        status_msg.set("Successfully read\nfrom Database")
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating table")
                else:
                    status_msg.set("Please select a Year")
            # If year selected but not type
            else:
                status_msg.set("Please select Volume\nor Accidents")

        # Event listener for sort button
        def sort_cmd():
            if type_combo.get() == "Traffic Volume":
                if year_combo.get() == "2016":
                    # For all the method calls to build frame in sort button
                    # the argument sorted will return sorted data
                    self.display.destroy()
                    try:
                        self.display = Tb.TableBuilder(self.root).build_table_flow("volume", "TrafficFlow2016", "2016", sort=True)
                        self.display.pack(fill="both", expand=True)
                        status_msg.set("Successfully sorted")
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating table")
                elif year_combo.get() == "2017":
                    self.display.destroy()
                    try:
                        self.display = Tb.TableBuilder(self.root).build_table_flow("volume", "TrafficFlow2017", "2017", sort=True)
                        self.display.pack(fill="both", expand=True)
                        status_msg.set("Successfully sorted")
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating table")
                elif year_combo.get() == "2018":
                    self.display.destroy()
                    try:
                        self.display = Tb.TableBuilder(self.root).build_table_flow("volume", "TrafficFlow2018", "2018", sort=True)
                        self.display.pack(fill="both", expand=True)
                        status_msg.set("Successfully sorted")
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating table")
                else:
                    status_msg.set("Please select a Year")
            elif type_combo.get() == "Traffic Accidents":
                if year_combo.get() == "2016":
                    self.display.destroy()
                    try:
                        self.display = Tb.TableBuilder(self.root).build_table_flow("incidents", "TrafficIncidents", "2016", sort=True)
                        self.display.pack(fill="both", expand=True)
                        status_msg.set("Successfully sorted")
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating table")
                elif year_combo.get() == "2017":
                    self.display.destroy()
                    try:
                        self.display = Tb.TableBuilder(self.root).build_table_flow("incidents", "TrafficIncidents", "2017", sort=True)
                        self.display.pack(fill="both", expand=True)
                        status_msg.set("Successfully sorted")
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating table")
                elif year_combo.get() == "2018":
                    self.display.destroy()
                    try:
                        self.display = Tb.TableBuilder(self.root).build_table_flow("incidents", "TrafficIncidents", "2018", sort=True)
                        self.display.pack(fill="both", expand=True)
                        status_msg.set("Successfully sorted")
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating table")
                else:
                    status_msg.set("Please select a Year")
            else:
                status_msg.set("Please select Volume\nor Accidents")

        def analysis_cmd():
            if type_combo.get() == "Traffic Volume":
                self.display.destroy()
                try:
                    self.display = Gb.GraphBuilder(self.root).build_graph("volume")
                    self.display.pack(fill="both", expand=True)
                    status_msg.set("Successfully analyzed")
                except OperationFailure:
                    status_msg.set("An error occurred\nwhile creating plot")
            elif type_combo.get() == "Traffic Accidents":
                self.display.destroy()
                try:
                    self.display = Gb.GraphBuilder(self.root).build_graph("incidents")
                    self.display.pack(fill="both", expand=True)
                    status_msg.set("Successfully analyzed")
                except OperationFailure:
                    status_msg.set("An error occurred\nwhile creating plot")

        def map_cmd():
            if type_combo.get() == "Traffic Volume":
                if year_combo.get() == "2016":
                    try:
                        Mb.MapBuilder("TrafficFlow2016", "volume").build_map()
                        status_msg.set("Map file successfully\n written")
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating map")
                elif year_combo.get() == "2017":
                    try:
                        Mb.MapBuilder("TrafficFlow2017", "volume").build_map()
                        status_msg.set("Map file successfully\n written")
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating map")
                elif year_combo.get() == "2018":
                    try:
                        Mb.MapBuilder("TrafficFlow2018", "volume").build_map()
                        status_msg.set("Map file successfully\n written")
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating map")

            elif type_combo.get() == "Traffic Accidents":
                if year_combo.get() == "2016":
                    try:
                        Mb.MapBuilder("TrafficIncidents", "incidents", year="2016").build_map()
                        status_msg.set("Map file successfully\n written")
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating map")
                elif year_combo.get() == "2017":
                    try:
                        Mb.MapBuilder("TrafficIncidents", "incidents", year="2017").build_map()
                        status_msg.set("Map file successfully\n written")
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating map")
                elif year_combo.get() == "2018":
                    try:
                        Mb.MapBuilder("TrafficIncidents", "incidents", year="2018").build_map()
                        status_msg.set("Map file successfully\n written")
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating map")

        status_msg = tk.StringVar()

        type_label = tk.Label(self, text="Choose type of data to visualize:")
        type_label.pack()

        type_combo = ttk.Combobox(self, values=("Traffic Accidents", "Traffic Volume"))
        type_combo.pack()

        year_label = tk.Label(self, text="Choose a year:")
        year_label.pack()

        year_combo = ttk.Combobox(self, values=("2016", "2017", "2018"))
        year_combo.pack()

        read_btn = tk.Button(self, text="Read", width=19, command=read_cmd)
        read_btn.pack()

        sort_btn = tk.Button(self, text="Sort", width=19, command=sort_cmd)
        sort_btn.pack()

        analysis_btn = tk.Button(self, text="Analysis", width=19, command=analysis_cmd)
        analysis_btn.pack()

        map_btn = tk.Button(self, text="Map", width=19, command=map_cmd)
        map_btn.pack()

        status_label = tk.Label(self, font=("Calibri", 12, "bold"), text="Status:")
        status_label.pack()

        status_text = tk.Label(self, textvariable=status_msg, width=20, height=4)
        status_text.pack()
