import tkinter as tk
import LeftFrame as Lf
import RightFrame as Rf


class RootWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.left_frame = Lf.LeftFrame().pack(fill='both', side='left')
        self.right_frame = Rf.RightFrame().pack(side='right')


if __name__ == "__main__":
    root = RootWindow()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.mainloop()
