import tkinter as tk


class RightFrame(tk.Frame):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.build_frame()

    def build_frame(self):
        frame = tk.Frame(self, width=500, height=250)
        frame.pack()

