import tkinter as tk
import LeftFrame as Lf

"""
Authors: Davis Allan and Santiago Flores
ID's: 10016543, 30119885
"""

class MainApplication(tk.Frame):
    """
    Creates and displays the main frame for the application
    """
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.left_frame = Lf.LeftFrame(self, self.master).pack(fill="both", side="left")


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(fill="both", side="left")
    # setting the root window to be full screen when the application launches
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry(("%dx%d" % (w, h)))
    root.title("YYC Traffic Analyzer")
    root.mainloop()
