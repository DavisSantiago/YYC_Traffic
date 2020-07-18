import tkinter as tk
import TableBuilder as Tb
import DatabaseQuery as Db


class RightFrame(tk.Frame):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.build_frame()

    @staticmethod
    def build_frame():
        results = Db.Query().query()
        tree = Tb.TableBuilder(results).build_table_flow()
        tree.pack(fill='both', expand=True)

