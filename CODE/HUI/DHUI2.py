import tkinter as tk
from tkinter import font as tkfont

class HUIApp(tk.Tk):
     def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        #self.frames['start'] = start(container=self.container, container=self)

        for F in (start, twochoice):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column= 0, sticky= "nsew")

        self.show_frame("start")

    
     def show_frame(self, page_name, data =None):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

       # if page_name == 'twochoice':
        #  frame.tkraise()
        #else:
         #   frame = self.frames[page_name]
          #  frame.tkraise()

        #def create_twochoice(self, page_name, data):
         #self.frames[page_name] = twochoice(parent=self.container, controller=self)


class start(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label (self, text= "Welcome to PAPI, Please Scan QR")    
        label.pack(side="top", fill= "x", pady=10)   

        button1 = tk.Button (self, text= "Go to ID",
        command= lambda: controller.show_frame("twochoice"))

        button1.pack() 

#class twochoice(tk.Frame):
     #def __init__(self, parent, controller):
        #tk.Frame.__init__(self, parent)
        #self.controller = controller
        #label1 = tk.Label(self, text= "ID#:")
        #label1.pack(side= "top", fill= "x", pady=10)
        #Label2 = tk.Label(self, text= "Name Variable Here")
        #Label2.pack(side= "top", fill= "x", pady=10)
        #button1 = tk.Button(self, text= "Correct Information",
        #command= lambda: controller.show_frame("start"))
        #button1.pack()
        #button2 = tk.Button(self, text= "Incorrect Information",
        #command= lambda: controller.show_frame("start"))
        #button2.pack()

class twochoice(tk.Frame):
     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
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
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
    
if __name__ == "__main__":
    app = HUIApp()
    app.mainloop()
