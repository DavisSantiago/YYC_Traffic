import tkinter as tk
from tkinter import ttk
import RightFrame as Rf
import GraphBuilder as Gb
import MapBuilder as Mb


class LeftFrame(tk.Frame):

    def __init__(self, master, root, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.root = root
        self.right_frame = tk.Frame()  # temp frame so that we can use .destroy right before calling the new updated frame
        self.build_frame()

    def build_frame(self):
        status_msg = tk.StringVar()

        type_label = tk.Label(self, text="Choose type of data to visualize:")
        type_label.pack()

        type_combo = ttk.Combobox(self, values=('Traffic Accidents', 'Traffic Volume'))
        type_combo.pack()

        year_label = tk.Label(self, text="Choose a year:")
        year_label.pack()

        year_combo = ttk.Combobox(self, values=('2016', '2017', '2018'))
        year_combo.pack()

        # Event listener for read button
        def read_cmd():
            if type_combo.get() == 'Traffic Volume':
                if year_combo.get() == '2016':
                    # Clears the previous message
                    # Builds frame, no filter means the data will be displayed as it is on the file
                    # Because this button is for read only, all the method calls will have this no filter
                    self.right_frame.destroy()
                    self.right_frame = Rf.RightFrame(self.root).build_frame("no_filter", 'TrafficFlow2016')
                    self.right_frame.pack(fill='both', expand=True)
                    status_msg.set("Successfully read\nfrom Database")
                elif year_combo.get() == '2017':
                    self.right_frame.destroy()
                    self.right_frame = Rf.RightFrame(self.root).build_frame("no_filter", 'TrafficFlow2017')
                    self.right_frame.pack(fill='both', expand=True)
                    status_msg.set("Successfully read\nfrom Database")
                elif year_combo.get() == '2018':
                    self.right_frame.destroy()
                    self.right_frame = Rf.RightFrame(self.root).build_frame("no_filter", 'TrafficFlow2018')
                    self.right_frame.pack(fill='both', expand=True)
                    status_msg.set("Successfully read\nfrom Database")
                # If there is no year selected
                else:
                    status_msg.set("Please select a Year")

            elif type_combo.get() == 'Traffic Accidents':
                if year_combo.get() == '2016':
                    # I pulled all the data from the same file, we can delete the other ones from out database
                    # The added argument filters, from the file, only data that happened in that year
                    self.right_frame.destroy()
                    self.right_frame = Rf.RightFrame(self.root).build_frame("no_filter", 'TrafficIncidents', '2016')
                    self.right_frame.pack(fill='both', expand=True)
                    status_msg.set("Successfully read\nfrom Database")
                elif year_combo.get() == '2017':
                    self.right_frame.destroy()
                    self.right_frame = Rf.RightFrame(self.root).build_frame("no_filter", 'TrafficIncidents', '2017')
                    self.right_frame.pack(fill='both', expand=True)
                    status_msg.set("Successfully read\nfrom Database")
                elif year_combo.get() == '2018':
                    self.right_frame.destroy()
                    self.right_frame = Rf.RightFrame(self.root).build_frame("no_filter", 'TrafficIncidents', '2018')
                    self.right_frame.pack(fill='both', expand=True)
                    status_msg.set("Successfully read\nfrom Database")
                else:
                    status_msg.set("Please select a Year")
            # If year selected but not type
            else:
                status_msg.set("Please select Volume\nor Accidents")

        read_btn = tk.Button(self, text="Read", width=19, command=read_cmd)
        read_btn.pack()

        # Event listener for sort button
        def sort_cmd():
            if type_combo.get() == 'Traffic Volume':
                if year_combo.get() == '2016':
                    # For all the method calls to build frame in sort button
                    # the argument sorted will return sorted data
                    self.right_frame.destroy()
                    self.right_frame = Rf.RightFrame(self.root).build_frame('sorted', 'TrafficFlow2016', '2016')
                    self.right_frame.pack(fill='both', expand=True)
                    status_msg.set("Successfully sorted")
                elif year_combo.get() == '2017':
                    self.right_frame.destroy()
                    self.right_frame = Rf.RightFrame(self.root).build_frame('sorted', 'TrafficFlow2017', '2017')
                    self.right_frame.pack(fill='both', expand=True)
                    status_msg.set("Successfully sorted")
                elif year_combo.get() == '2018':
                    self.right_frame.destroy()
                    self.right_frame = Rf.RightFrame(self.root).build_frame('sorted', 'TrafficFlow2018', '2018')
                    self.right_frame.pack(fill='both', expand=True)
                    status_msg.set("Successfully sorted")
                else:
                    status_msg.set("Please select a Year")
            elif type_combo.get() == 'Traffic Accidents':
                if year_combo.get() == '2016':
                    self.right_frame.destroy()
                    self.right_frame = Rf.RightFrame(self.root).build_frame('sorted', 'TrafficIncidents', '2016')
                    self.right_frame.pack(fill='both', expand=True)
                    status_msg.set("Successfully sorted")
                elif year_combo.get() == '2017':
                    self.right_frame.destroy()
                    self.right_frame = Rf.RightFrame(self.root).build_frame('sorted', 'TrafficIncidents', '2017')
                    self.right_frame.pack(fill='both', expand=True)
                    status_msg.set("Successfully sorted")
                elif year_combo.get() == '2018':
                    self.right_frame.destroy()
                    self.right_frame = Rf.RightFrame(self.root).build_frame('sorted', 'TrafficIncidents', '2018')
                    self.right_frame.pack(fill='both', expand=True)
                    status_msg.set("Successfully sorted")
                else:
                    status_msg.set("Please select a Year")
            else:
                status_msg.set("Please select Volume\nor Accidents")

        sort_btn = tk.Button(self, text="Sort", width=19, command=sort_cmd)
        sort_btn.pack()

        def analysis_cmd():
            if type_combo.get() == 'Traffic Volume':
                self.right_frame.destroy()
                self.right_frame = Gb.GraphBuilder(self.root).build_graph('traffic')
                self.right_frame.pack(fill='both', expand=True)
            elif type_combo.get() == 'Traffic Accidents':
                self.right_frame.destroy()
                self.right_frame = Gb.GraphBuilder(self.root).build_graph('accidents')
                self.right_frame.pack(fill='both', expand=True)

        def map_cmd():
            if type_combo.get() == 'Traffic Volume':
                if year_combo.get() == '2016':
                    Mb.MapBuilder('TrafficFlow2016', 'volume').build_map()
                    status_msg.set('Map file successfully\n written')
                elif year_combo.get() == '2017':
                    Mb.MapBuilder('TrafficFlow2017', 'volume').build_map()
                    status_msg.set('Map file successfully\n written')
                elif year_combo.get() == '2018':
                    Mb.MapBuilder('TrafficFlow2018', 'volume').build_map()
                    status_msg.set('Map file successfully\n written')

            elif type_combo.get() == 'Traffic Accidents':
                if year_combo.get() == '2016':
                    Mb.MapBuilder('TrafficIncidents', 'incidents', year='2016').build_map()
                    status_msg.set('Map file successfully\n written')
                elif year_combo.get() == '2017':
                    Mb.MapBuilder('TrafficIncidents', 'incidents', year='2017').build_map()
                    status_msg.set('Map file successfully\n written')
                elif year_combo.get() == '2018':
                    Mb.MapBuilder('TrafficIncidents', 'incidents', year='2018').build_map()
                    status_msg.set('Map file successfully\n written')

        analysis_btn = tk.Button(self, text="Analysis", width=19, command=analysis_cmd)
        analysis_btn.pack()

        map_btn = tk.Button(self, text="Map", width=19, command=map_cmd)
        map_btn.pack()

        status_label = tk.Label(self, font=("Calibri", 12, 'bold'), text="Status:")
        status_label.pack()

        status_text = tk.Label(self, textvariable=status_msg, width=20, height=4)
        status_text.pack()



