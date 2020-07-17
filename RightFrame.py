import tkinter as tk
import TableBuilder as Tb
import DatabaseQuery as Db


class RightFrame(tk.Frame):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.build_frame()

    def build_frame(self):
        results = Db.Query().query()
        tree = Tb.TableBuilder(results).build_table_flow()
        tree.grid(row=2, column=2)

