import tkinter as tk
from tkinter import ttk
import RightFrame as Rf


class LeftFrame(tk.Frame):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.build_frame()

    def build_frame(self):
        type_label = tk.Label(self, text="Choose type of data to visualize:")
        type_label.grid(row=0, column=0)

        type_combo = ttk.Combobox(self, values=('Traffic Accidents', 'Traffic Volume'))
        type_combo.grid(row=0, column=1)

        year_label = tk.Label(self, text="Choose a year:")
        year_label.grid(row=1, column=0)

        year_combo = ttk.Combobox(self, values=('2016', '2017', '2018'))
        year_combo.grid(row=1, column=1)

        def read_cmd():
            if type_combo.get() == 'Traffic Volume':
                if year_combo.get() == '2016':
                    status_text.delete('1.0', tk.END)
                    status_text.insert(tk.END, "Displaying Traffic\nVolume of 2016")
                    Rf.RightFrame.build_frame("no_filter", 'TrafficFlow2016')
                elif year_combo.get() == '2017':
                    status_text.delete('1.0', tk.END)
                    status_text.insert(tk.END, "Displaying Traffic\nVolume of 2017")
                    Rf.RightFrame.build_frame("no_filter", 'TrafficFlow2017')
                elif year_combo.get() == '2018':
                    status_text.delete('1.0', tk.END)
                    status_text.insert(tk.END, "Displaying Traffic\nVolume of 2018")
                    Rf.RightFrame.build_frame("no_filter", 'TrafficFlow2018')
                else:
                    status_text.delete('1.0', tk.END)
                    status_text.insert(tk.END, "Please select a year")
            elif type_combo.get() == 'Traffic Accidents':
                if year_combo.get() == '2016':
                    status_text.delete('1.0', tk.END)
                    status_text.insert(tk.END, "Displaying Traffic\nAccidents of 2016")
                    Rf.RightFrame.build_frame("no_filter", 'TrafficIncidents', '2016')
                elif year_combo.get() == '2017':
                    status_text.delete('1.0', tk.END)
                    status_text.insert(tk.END, "Displaying Traffic\nAccidents of 2017")
                    Rf.RightFrame.build_frame("no_filter", 'TrafficIncidents', '2017')
                elif year_combo.get() == '2018':
                    status_text.delete('1.0', tk.END)
                    status_text.insert(tk.END, "Displaying Traffic\nAccidents of 2018")
                    Rf.RightFrame.build_frame("no_filter", 'TrafficIncidents', '2018')
                else:
                    status_text.delete('1.0', tk.END)
                    status_text.insert(tk.END, "Please select a year")
            else:
                status_text.delete('1.0', tk.END)
                status_text.insert(tk.END, "Please select Volume\nor Accidents")

        read_btn = tk.Button(self, text="Read", width=10, command=read_cmd)
        read_btn.grid(row=2, column=0)

        def sort_cmd():
            if type_combo.get() == 'Traffic Volume':
                if year_combo.get() == '2016':
                    status_text.delete('1.0', tk.END)
                    status_text.insert(tk.END, "Displaying Traffic\nVolume of 2016\nSorted by Volume")
                    Rf.RightFrame.build_frame('sorted', 'TrafficFlow2016', '2016')
                elif year_combo.get() == '2017':
                    status_text.delete('1.0', tk.END)
                    status_text.insert(tk.END, "Displaying Traffic\nVolume of 2017\nSorted by Volume")
                    Rf.RightFrame.build_frame('sorted', 'TrafficFlow2017', '2017')
                elif year_combo.get() == '2018':
                    status_text.delete('1.0', tk.END)
                    status_text.insert(tk.END, "Displaying Traffic\nVolume of 2018\nSorted by Volume")
                    Rf.RightFrame.build_frame('sorted', 'TrafficFlow2018', '2018')
                else:
                    status_text.delete('1.0', tk.END)
                    status_text.insert(tk.END, "Please select a year")
            elif type_combo.get() == 'Traffic Accidents':
                if year_combo.get() == '2016':
                    status_text.delete('1.0', tk.END)
                    status_text.insert(tk.END, "Displaying Traffic\nAccidents of 2016\nSorted by Number of\nIncidents")
                    Rf.RightFrame.build_frame('sorted', 'TrafficIncidents', '2016')
                elif year_combo.get() == '2017':
                    status_text.delete('1.0', tk.END)
                    status_text.insert(tk.END, "Displaying Traffic\nAccidents of 2017\nSorted by Number of\nIncidents")
                    Rf.RightFrame.build_frame('sorted', 'TrafficIncidents', '2017')
                elif year_combo.get() == '2018':
                    status_text.delete('1.0', tk.END)
                    status_text.insert(tk.END, "Displaying Traffic\nAccidents of 2018\nSorted by Number of\nIncidents")
                    Rf.RightFrame.build_frame('sorted', 'TrafficIncidents', '2018')
                else:
                    status_text.delete('1.0', tk.END)
                    status_text.insert(tk.END, "Please select a year")
            else:
                status_text.delete('1.0', tk.END)
                status_text.insert(tk.END, "Please select Volume\nor Accidents")

        sort_btn = tk.Button(self, text="Sort", width=10, command=sort_cmd)
        sort_btn.grid(row=3, column=0)

        analysis_btn = tk.Button(self, text="Analysis", width=10)
        analysis_btn.grid(row=4, column=0)

        map_btn = tk.Button(self, text="Map", width=10)
        map_btn.grid(row=5, column=0)

        status_label = tk.Label(self, text="Status:")
        status_label.grid(row=6, column=0)

        status_text = tk.Text(self, width=20, height=4)
        status_text.grid(row=7, column=0)



