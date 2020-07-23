import DatabaseQuery as Db
import ListBuilder as Lb
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GraphBuilder:
    """
    Creates a graph with the year in the x axis and volume or incidents on the y axis
    """

    def __init__(self, master):
        self.master = master

    @staticmethod
    def sum_incidents(year_list):
        """
        Adds the number of incidents in the list and returns a dictionary with the values
        :param year_list: (list) incident list
        :return: (dict) the count of incidents for every address
        """
        incident_count = {}
        # For each address in the list, add to dict if it's not there yet or increase it's counter by 1 if it's there
        for address in year_list:
            if address not in incident_count:
                incident_count[address] = 1
            else:
                incident_count[address] += 1
        return incident_count

    def build_graph(self, data):
        """
        Creates a graph in a canvas, it can be of volume or incidents and will compare the data for 2016, 2017 and 2018
        :param data: (str) the type of information to be displayed, volume or incidents
        :return: (canvas) Canvas widget displaying the results in a graph
        """
        if data == "volume":
            years = {"2016": "TrafficFlow2016", "2017": "TrafficFlow2017", "2018": "TrafficFlow2018"}
            year_max = []
            year_list = []

            # Building a list for each year, from its respective file in database
            for year, collection in years.items():
                volume_list = Lb.ListBuilder.build_list(data, collection, year, sort=True)

                # The year and its max volume will have the same index in both lists
                year_list.append(year)
                year_max.append(volume_list[0][4])

            # creating the graph
            figure = Figure(figsize=(13, 12), dpi=100)
            figure.suptitle("Max Traffic Volume Per Year", fontsize=20)
            plot = figure.add_subplot(111)
            plot.plot(year_list, year_max, linewidth=3.0)
            plot.set_xlabel("Year", fontsize=15)
            plot.set_ylabel("Volume", fontsize=15)

            canvas = FigureCanvasTkAgg(figure, self.master)
            graph = canvas.get_tk_widget()

            return graph

        elif data == "incidents":
            incidents_2016 = []
            incidents_2017 = []
            incidents_2018 = []
            max_incidents_per_year = []
            year = ["2016", "2017", "2018"]

            results = Db.Query().query("TrafficIncidents")

            # Querying all the information from the same file, add each item to its respective list
            for item in results:
                if "2016" in item["start_time"]:
                    incidents_2016.append((item["address"]))
                if "2017" in item["start_time"]:
                    incidents_2017.append((item["address"]))
                if "2018" in item["start_time"]:
                    incidents_2018.append((item["address"]))

            # Adding the maximum value for each year to max incidents per year list
            max_incidents_per_year.append(max(self.sum_incidents(incidents_2016).values()))
            max_incidents_per_year.append(max(self.sum_incidents(incidents_2017).values()))
            max_incidents_per_year.append(max(self.sum_incidents(incidents_2018).values()))

            # creating the graph
            figure = Figure(figsize=(13, 12), dpi=100)
            figure.suptitle("Max Incidents Per Year", fontsize=20)
            plot = figure.add_subplot(111)
            plot.plot(year, max_incidents_per_year, linewidth=3.0)
            plot.set_xlabel("Year", fontsize=15)
            plot.set_ylabel("Incidents", fontsize=15)

            canvas = FigureCanvasTkAgg(figure, self.master)
            graph = canvas.get_tk_widget()

            return graph
