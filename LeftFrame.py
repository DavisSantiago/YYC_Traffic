import tkinter as tk
from tkinter import ttk


class LeftFrame(tk.Frame):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.build_frame(self)

    @staticmethod
    def build_frame(self):
        type_label = tk.Label(text="Choose type of data to visualize:")
        type_label.pack()

        type_combo = ttk.Combobox(values=('Traffic Accidents', 'Traffic Volume'))
        type_combo.pack()

        year_label = tk.Label(text="Choose a year:")
        year_label.pack()

        year_combo = ttk.Combobox(values=('2016', '2017', '2018'))
        year_combo.pack()

        read_btn = tk.Button(text="Read", width=10)
        read_btn.pack()

        sort_btn = tk.Button(text="Sort", width=10)
        sort_btn.pack()

        analysis_btn = tk.Button(text="Analysis", width=10)
        analysis_btn.pack()

        map_btn = tk.Button(text="Map", width=10)
        map_btn.pack()

        status_label = tk.Label(text="Status:")
        status_label.pack()

        status_text = tk.Text(width=10, height=2)
        status_text.pack()

