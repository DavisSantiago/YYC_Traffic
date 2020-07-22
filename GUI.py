import tkinter as tk
import LeftFrame as Lf


class MainApplication(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.left_frame = Lf.LeftFrame(self, self.parent).pack(fill="both", side="left")


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(fill="both", side="left")
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry(("%dx%d" % (w, h)))
    root.mainloop()
