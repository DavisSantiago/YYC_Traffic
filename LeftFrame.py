import tkinter as tk
from tkinter import ttk
import GraphBuilder as Gb
import MapBuilder as Mb
import TableBuilder as Tb
from pymongo.errors import OperationFailure


class LeftFrame(tk.Frame):
    """
    Creates and displays the left frame with all widgets and controls the rest of the GUI
    """

    def __init__(self, master, root):
        tk.Frame.__init__(self, master)
        self.root = root
        self.display = tk.Frame()
        self.build_frame()

    def build_frame(self):
        """
        Builds the frame that contains all the elements of the GUI and handles all events
        """

        def read_cmd():
            """
            Event listener for the Read button, updates the display with the un-sorted table upon being activated
            """
            if type_combo.get() == "Traffic Volume":
                if year_combo.get() == "2016":
                    self.display.destroy()
                    # Attempts to get the information from the database
                    try:
                        self.display = Tb.TableBuilder(self.root).build_table("volume", "TrafficFlow2016", "2016")
                        self.display.pack(fill="both", side="right", expand=True)
                        status_msg.set("Successfully read\nfrom Database")
                    # Error message if it can't connect to the database
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating table")
                elif year_combo.get() == "2017":
                    self.display.destroy()
                    try:
                        self.display = Tb.TableBuilder(self.root).build_table("volume", "TrafficFlow2017", "2017")
                        self.display.pack(fill="both", expand=True)
                        status_msg.set("Successfully read\nfrom Database")
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating table")
                elif year_combo.get() == "2018":
                    self.display.destroy()
                    try:
                        self.display = Tb.TableBuilder(self.root).build_table("volume", "TrafficFlow2018", "2018")
                        self.display.pack(fill="both", expand=True)
                        status_msg.set("Successfully read\nfrom Database")
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating table")
                # If no year is selected
                else:
                    status_msg.set("Please select a Year")

            elif type_combo.get() == "Traffic Incidents":
                if year_combo.get() == "2016":
                    self.display.destroy()
                    try:
                        self.display = Tb.TableBuilder(self.root).build_table("incidents", "TrafficIncidents", "2016")
                        self.display.pack(fill="both", expand=True)
                        status_msg.set("Successfully read\nfrom Database")
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating table")
                elif year_combo.get() == "2017":
                    self.display.destroy()
                    try:
                        self.display = Tb.TableBuilder(self.root).build_table("incidents", "TrafficIncidents", "2017")
                        self.display.pack(fill="both", expand=True)
                        status_msg.set("Successfully read\nfrom Database")
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating table")
                elif year_combo.get() == "2018":
                    self.display.destroy()
                    try:
                        self.display = Tb.TableBuilder(self.root).build_table("incidents", "TrafficIncidents", "2018")
                        self.display.pack(fill="both", expand=True)
                        status_msg.set("Successfully read\nfrom Database")
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating table")
                # If no year is selected
                else:
                    status_msg.set("Please select a Year")

            # If no type is selected
            else:
                status_msg.set("Please select Volume\nor Incidents")

        #
        def sort_cmd():
            """
            Event listener for the Sort button, updates the display with the sorted data table upon being activated
            """
            if type_combo.get() == "Traffic Volume":
                if year_combo.get() == "2016":
                    self.display.destroy()
                    try:
                        self.display = Tb.TableBuilder(self.root).build_table("volume", "TrafficFlow2016", "2016", sort=True)
                        self.display.pack(fill="both", expand=True)
                        status_msg.set("Successfully sorted")
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating table")
                elif year_combo.get() == "2017":
                    self.display.destroy()
                    try:
                        self.display = Tb.TableBuilder(self.root).build_table("volume", "TrafficFlow2017", "2017", sort=True)
                        self.display.pack(fill="both", expand=True)
                        status_msg.set("Successfully sorted")
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating table")
                elif year_combo.get() == "2018":
                    self.display.destroy()
                    try:
                        self.display = Tb.TableBuilder(self.root).build_table("volume", "TrafficFlow2018", "2018", sort=True)
                        self.display.pack(fill="both", expand=True)
                        status_msg.set("Successfully sorted")
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating table")
                else:
                    status_msg.set("Please select a Year")

            elif type_combo.get() == "Traffic Incidents":
                if year_combo.get() == "2016":
                    self.display.destroy()
                    try:
                        self.display = Tb.TableBuilder(self.root).build_table("incidents", "TrafficIncidents", "2016", sort=True)
                        self.display.pack(fill="both", expand=True)
                        status_msg.set("Successfully sorted")
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating table")
                elif year_combo.get() == "2017":
                    self.display.destroy()
                    try:
                        self.display = Tb.TableBuilder(self.root).build_table("incidents", "TrafficIncidents", "2017", sort=True)
                        self.display.pack(fill="both", expand=True)
                        status_msg.set("Successfully sorted")
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating table")
                elif year_combo.get() == "2018":
                    self.display.destroy()
                    try:
                        self.display = Tb.TableBuilder(self.root).build_table("incidents", "TrafficIncidents", "2018", sort=True)
                        self.display.pack(fill="both", expand=True)
                        status_msg.set("Successfully sorted")
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating table")
                # If no year is selected
                else:
                    status_msg.set("Please select a Year")

            # If no type is selected
            else:
                status_msg.set("Please select Volume\nor Incidents")

        # Event listener for analysis button
        def analysis_cmd():
            """
            Event listener for the Analysis button, updates the display with the graph upon being activated
            """
            if type_combo.get() == "Traffic Volume":
                self.display.destroy()
                try:
                    self.display = Gb.GraphBuilder(self.root).build_graph("volume")
                    self.display.pack(fill="both", expand=True)
                    status_msg.set("Successfully analyzed")
                except OperationFailure:
                    status_msg.set("An error occurred\nwhile creating plot")

            elif type_combo.get() == "Traffic Incidents":
                self.display.destroy()
                try:
                    self.display = Gb.GraphBuilder(self.root).build_graph("incidents")
                    self.display.pack(fill="both", expand=True)
                    status_msg.set("Successfully analyzed")
                except OperationFailure:
                    status_msg.set("An error occurred\nwhile creating plot")

            # If no type is selected
            else:
                status_msg.set("Please select Volume\nor Incidents")

        # Event listener for map button
        def map_cmd():
            """
            Event listener for the Map button, creates and writes the map file upon being activated
            """
            if type_combo.get() == "Traffic Volume":
                if year_combo.get() == "2016":
                    try:
                        Mb.MapBuilder("TrafficFlow2016", "volume", "2016").build_map()
                        status_msg.set("Map file successfully\n written")
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating map")
                elif year_combo.get() == "2017":
                    try:
                        Mb.MapBuilder("TrafficFlow2017", "volume", "2017").build_map()
                        status_msg.set("Map file successfully\n written")
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating map")
                elif year_combo.get() == "2018":
                    try:
                        Mb.MapBuilder("TrafficFlow2018", "volume", "2018").build_map()
                        status_msg.set("Map file successfully\n written")
                    except OperationFailure:
                        status_msg.set("An error occurred\nwhile creating map")

            elif type_combo.get() == "Traffic Incidents":
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

            # If no type is selected
            else:
                status_msg.set("Please select Volume\nor Incidents")

        status_msg = tk.StringVar()

        type_label = tk.Label(self, text="Choose type of data to visualize:")
        type_label.pack()

        type_combo = ttk.Combobox(self, values=("Traffic Incidents", "Traffic Volume"))
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
