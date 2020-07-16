import tkinter as tk
import LeftFrame as Lf
import RightFrame as Rf


class MainGUI(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.left_frame = Lf.LeftFrame().grid(row=0, column=0)
        self.right_frame = Rf.RightFrame().grid(row=0, column=1)


if __name__ == "__main__":
    root = tk.Tk()
    MainGUI(root).grid()
    root.mainloop()
