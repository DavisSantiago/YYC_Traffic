import tkinter as tk
from tkinter import ttk


class LeftFrame(tk.Frame):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.build_frame()

    @staticmethod
    def build_frame():
        combo_label = tk.Label(text="Choose type of data to visualize:")
        combo_label.pack()

        type_combo = ttk.Combobox(values=('Traffic Accidents', 'Traffic Volume'))
        type_combo.pack()

        year_combo = ttk.Combobox(values=('2016', '2017', '2018'))
        year_combo.pack()

