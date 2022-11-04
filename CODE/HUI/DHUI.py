import tkinter as tk
from tkinter import font as tkfont

class HUIApp(tk.Tk):
     def init(self, args, **kwargs):
        tk.Tk.init(self,args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (start, twochoice):
            page_name = F.name
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column= 0, sticky= "nsew")

        self.show_frame("start")

     def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class start(tk.Frame):
    def init(self, parent, controller):
        tk.Frame.init(self, parent)
        self.controller = controller
        label = tk.Label (self, text= "Welcome to PAPI, Please Scan QR")
        label.pack(side="top", fill= "x", pady=10)

        button1 = tk.Button (self, text= "Go to ID",
        command= lambda: controller.show_frame("twochoice"))

        button1.pack() 

class twochoice(tk.Frame):
     def init(self, parent, controller):
        tk.Frame.init(self, parent)
        self.controller = controller
        label1 = tk.Label(self, text= "ID#:")
        label1.pack(side= "top", fill= "x", pady=10)
        Label2 = tk.Label(self, text= "Name Variable Here")
        Label2.pack(side= "top", fill= "x", pady=10)
        button1 = tk.Button(self, text= "Correct Information",
        command= lambda: controller.show_frame("start"))
        button1.pack()
        button2 = tk.Button(self, text= "Incorrect Information",
        command= lambda: controller.show_frame("start"))
        button2.pack()
class yes(tk.Tk):
    def init(self, parent, controller):
        tk.Frame.init(self, parent)
        self.controller = controller

if name == "main":
    app = HUIApp()
    app.mainloop()
