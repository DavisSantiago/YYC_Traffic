import DatabaseQuery as Db
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# https://matplotlib.org/3.3.0/tutorials/introductory/pyplot.html


class GraphBuilder(tk.Frame):

    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.master = master

    def build_graph(self, data):

        if data == 'traffic':
            years = {'2016': 'TrafficFlow2016', '2017': 'TrafficFlow2017', '2018': 'TrafficFlow2018'}
            year_max = []
            year_list = []

            for year, file in years.items():
                volume_list = []

                results = Db.Query().query(file)

                for item in results:
                    volume_list.append((item["segment"], item["coordinates"], item["year"], item["length"], item["volume"]))

                temp = volume_list.copy()
                volume_list = sorted(temp, key=lambda x: x[4], reverse=True)

                year_list.append(year)
                year_max.append(volume_list[0][4])

            figure = Figure(figsize=(13, 12), dpi=100)
            figure.suptitle("Max traffic volume per year", fontsize=20)
            plot = figure.add_subplot(111)
            plot.plot(year_list, year_max, linewidth=3.0)
            plot.set_xlabel("Year", fontsize=15)
            plot.set_ylabel("Volume", fontsize=15)

            canvas = FigureCanvasTkAgg(figure, self.master)
            plot_test = canvas.get_tk_widget()
            plot_test.pack()

            return self
