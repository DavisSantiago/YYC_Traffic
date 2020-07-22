import tkinter as tk
import TableBuilder as Tb


class RightFrame(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master

    def build_frame(self, sort=None, collection=None, year=None):

        # If the collection is for Volume
        if sort is not None and collection.startswith('TrafficFlow'):
            # If button sort clicked it will do this
            if sort == 'sorted':
                tree = Tb.TableBuilder(self).build_table_flow("volume", collection, year, 'sorted')
                tree.pack(fill='both', expand=True)
            # If button read clicked it will do this
            else:
                tree = Tb.TableBuilder(self).build_table_flow("volume", collection)
                tree.pack(fill='both', expand=True)

        # If collection is for Incidents
        elif sort is not None and collection.startswith('TrafficIncidents'):
            # Because all the information comes from the same file here is where the data gets filtered for each year
            if year == '2016':
                # If button sort clicked it will go this
                if sort == 'sorted':
                    tree = Tb.TableBuilder(self).build_table_flow("incidents", collection, '2016', 'sorted')
                    tree.pack(fill='both', expand=True)
                # If button read clicked it will do this
                else:
                    tree = Tb.TableBuilder(self).build_table_flow("incidents", collection, '2016')
                    tree.pack(fill='both', expand=True)
            elif year == '2017':
                if sort == 'sorted':
                    tree = Tb.TableBuilder(self).build_table_flow("incidents", collection, '2017', 'sorted')
                    tree.pack(fill='both', expand=True)
                else:
                    tree = Tb.TableBuilder(self).build_table_flow("incidents", collection, '2017')
                    tree.pack(fill='both', expand=True)
            elif year == '2018':
                if sort == 'sorted':
                    tree = Tb.TableBuilder(self).build_table_flow("incidents", collection, '2018', 'sorted')
                    tree.pack(fill='both', expand=True)
                else:
                    tree = Tb.TableBuilder(self).build_table_flow("incidents", collection, '2018')
                    tree.pack(fill='both', expand=True)

        return self

