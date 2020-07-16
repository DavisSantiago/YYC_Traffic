import tkinter as tk
import LeftFrame as Lf
import RightFrame as Rf


class MainGUI(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.left_frame = Lf.LeftFrame()
        self.right_frame = Rf.RightFrame()


if __name__ == "__main__":
    root = tk.Tk()
    MainGUI(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
