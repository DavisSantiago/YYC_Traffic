import DatabaseQuery as Db
import ListBuilder as Lb
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GraphBuilder:

    def __init__(self, master):
        self.master = master

    @staticmethod
    def sum_incidents(year_list):
        incident_count = {}
        for address in year_list:
            if address not in incident_count:
                incident_count[address] = 1
            else:
                incident_count[address] += 1
        return incident_count

    def build_graph(self, data):
        if data == "volume":
            years = {"2016": "TrafficFlow2016", "2017": "TrafficFlow2017", "2018": "TrafficFlow2018"}
            year_max = []
            year_list = []

            for year, collection in years.items():
                volume_list = Lb.ListBuilder.build_list(data, collection, year, sort=True)

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

            return plot_test

        elif data == "incidents":
            incidents_2016 = []
            incidents_2017 = []
            incidents_2018 = []
            max_incidents_per_year = []
            year = ["2016", "2017", "2018"]

            results = Db.Query().query("TrafficIncidents")

            for item in results:
                if "2016" in item["start_time"]:
                    incidents_2016.append((item["address"]))
                if "2017" in item["start_time"]:
                    incidents_2017.append((item["address"]))
                if "2018" in item["start_time"]:
                    incidents_2018.append((item["address"]))

            max_incidents_per_year.append(max(self.sum_incidents(incidents_2016).values()))
            max_incidents_per_year.append(max(self.sum_incidents(incidents_2017).values()))
            max_incidents_per_year.append(max(self.sum_incidents(incidents_2018).values()))

            figure = Figure(figsize=(13, 12), dpi=100)
            figure.suptitle("Max accidents per year", fontsize=20)
            plot = figure.add_subplot(111)
            plot.plot(year, max_incidents_per_year, linewidth=3.0)
            plot.set_xlabel("Year", fontsize=15)
            plot.set_ylabel("Incidents", fontsize=15)

            canvas = FigureCanvasTkAgg(figure, self.master)
            plot_test = canvas.get_tk_widget()

            return plot_test
