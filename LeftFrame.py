import tkinter as tk
from tkinter import ttk


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

        read_btn = tk.Button(self, text="Read", width=10)
        read_btn.grid(row=2, column=0)

        sort_btn = tk.Button(self, text="Sort", width=10)
        sort_btn.grid(row=3, column=0)

        analysis_btn = tk.Button(self, text="Analysis", width=10)
        analysis_btn.grid(row=4, column=0)

        map_btn = tk.Button(self, text="Map", width=10)
        map_btn.grid(row=5, column=0)

        status_label = tk.Label(self, text="Status:")
        status_label.grid(row=6, column=0)

        status_text = tk.Text(self, width=10, height=2)
        status_text.grid(row=7, column=0)

