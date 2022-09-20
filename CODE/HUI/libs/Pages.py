import tkinter as tk
from libs.WidgetSet import WidgetSet
from libs.qr_reader import reader
import concurrent.futures

class Controller(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("800x480")

        # root container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (ScanPage, DisplayPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # align on top of each other,
            # top is what's visible
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("ScanPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class ScanPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Scan Page")
        label.pack(side="top", fill="x", pady=10)

        label1 = tk.Label(self, text="Please scan your prescription.")
        label1.pack()


class DisplayPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Display Page")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the Scan",
                           command=lambda: controller.show_frame("ScanPage"))
        button.pack()