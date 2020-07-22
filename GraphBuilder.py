import DatabaseQuery as Db
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GraphBuilder(tk.Frame):

    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.master = master
        self.plot_test = tk.Frame
        self.canvas = None

    def delete(self):
        self.canvas.get_tk_widget.pack_forget()
        self.destroy()

    def build_graph(self, data):
        if data == 'traffic':
            years = {'2016': 'TrafficFlow2016', '2017': 'TrafficFlow2017', '2018': 'TrafficFlow2018'}
            year_max = []
            year_list = []

            for year, file in years.items():
                volume_list = []

                results = Db.Query().query(file)

                for item in results:
                    volume_list.append(
                        (item["segment"], item["coordinates"], item["year"], item["length"], item["volume"]))

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
            canvas.get_tk_widget().delete("all")
            plot_test.pack()

            return self

        elif data == 'accidents':
            incidents_2016 = []
            incidents_2017 = []
            incidents_2018 = []
            max_incidents_per_year = []
            year = ['2016', '2017', '2018']

            results = Db.Query().query('TrafficIncidents')

            for item in results:
                if '2016' in item["start_time"]:
                    incidents_2016.append((item["address"]))
                if '2017' in item["start_time"]:
                    incidents_2017.append((item["address"]))
                if '2018' in item["start_time"]:
                    incidents_2018.append((item["address"]))

            accident_count_2016 = {}
            for address in incidents_2016:
                if address not in accident_count_2016:
                    accident_count_2016[address] = 1
                else:
                    accident_count_2016[address] += 1
            max_incidents_per_year.append(max(accident_count_2016.values()))

            accident_count_2017 = {}
            for address in incidents_2017:
                if address not in accident_count_2017:
                    accident_count_2017[address] = 1
                else:
                    accident_count_2017[address] += 1
            max_incidents_per_year.append(max(accident_count_2017.values()))

            accident_count_2018 = {}
            for address in incidents_2018:
                if address not in accident_count_2018:
                    accident_count_2018[address] = 1
                else:
                    accident_count_2018[address] += 1
            max_incidents_per_year.append(max(accident_count_2018.values()))

            figure = Figure(figsize=(13, 12), dpi=100)
            figure.suptitle("Max accidents per year", fontsize=20)
            plot = figure.add_subplot(111)
            plot.plot(year, max_incidents_per_year, linewidth=3.0)
            plot.set_xlabel("Year", fontsize=15)
            plot.set_ylabel("Incidents", fontsize=15)

            self.canvas = FigureCanvasTkAgg(figure, self.master)
            self.plot_test = self.canvas.get_tk_widget()
            self.plot_test.pack()

            return self
