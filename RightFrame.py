import tkinter as tk
import TableBuilder as Tb
import DatabaseQuery as Db


class RightFrame(tk.Frame):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.build_frame()

    @staticmethod
    def build_frame(table=None, collection=None):
        # If no argument passed to the method it will be a blank screen
        if table is None or collection is None:
            # TODO clear screen before printing new table
            pass

        elif table is not None and collection.startswith('TrafficFlow'):
            results = Db.Query().query(collection)
            tree = Tb.TableBuilder(results).build_table_flow("volume")
            tree.pack(fill='both', expand=True)

        elif table is not None and collection.startswith('TrafficIncidents'):
            results = Db.Query().query(collection)
            tree = Tb.TableBuilder(results).build_table_flow("incidents")
            tree.pack(fill='both', expand=True)

