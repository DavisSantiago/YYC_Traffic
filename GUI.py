import tkinter as tk
import LeftFrame as Lf
import RightFrame as Rf


class MainApplication(tk.Frame):
    def __init__(self, parent, *args,  **kwargs):
        tk.Frame.__init__(self, parent, *args,  **kwargs)
        self.parent = parent
        self.left_frame = Lf.LeftFrame(self).pack(fill='both', side='left')
        self.right_frame = Rf.RightFrame(self).pack(side='right')


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(fill='both', side='left')
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.mainloop()
