from cProfile import label
import tkinter as tk

# A set of widgets, said widgets are what show when 
class WidgetSet():
    def __init__(self, pair) -> None:
        self.pill_name = pair[0]
        self.pill_amount = pair[1]

        self.frame = tk.Frame(root,borderwidth=0, relief="groove")
        self.frame.pack(side="top", fill="x", pady=(12, 0))

        self.entry = tk.Label(self.frame ,width=30, text=self.pill_name, font=('Arial 16'), bg="white")
        self.entry.pack(side="left", padx=(150,0))

        self.inner_frame = tk.Frame(self.frame, borderwidth=0, relief="groove")
        self.inner_frame.pack(side="right", fill="x")
        
        self.label = tk.Label(self.inner_frame, width=5,height=2, text=self.pill_amount, bg="white")
        self.label.pack(side="left", padx=(0,250))

    def Minus(self):
        if self.cnt.get() > 0:
            self.cnt.set(self.cnt.get()-1)

    def Plus(self):
        if self.cnt.get() < 99:
            self.cnt.set(self.cnt.get()+1)

def output_data(packet):
    print(packet)

def createwidgets(pair):
    if len(obj) < 8:
        obj.append(WidgetSet(pair))

def clean_widgets():
    pass

def removewidgets():
    if len(obj) > 1:
        def frame_deleter(root_frame):
            slaves = root_frame.winfo_children()
            for widget in slaves:
                if widget is tk.Frame:
                    frame_deleter(widget)
                widget.destroy()

        widget_set = obj.pop(len(obj)-1)
        root_frame = widget_set.frame
        frame_deleter(root_frame)
        root_frame.destroy()

def prepare_packet(packet):
    string_arr = []
    for element in packet:
        if type(element) == list:
            element = prepare_packet(element)
        string_arr.append(element)
    
    return ",".join(string_arr)

obj = []
root = tk.Tk()
def hui_main(packet):


    root.geometry("800x480")

    name_label = tk.Label(root, text=packet[0])
    name_label.pack(side="top")

    for pair in packet[1::]:
        createwidgets(pair)

    string_packet = prepare_packet(packet)

    createWidgetButton = tk.Button(root, height=2, text="Done", command=lambda: output_data(string_packet))
    createWidgetButton.pack(side="bottom", fill="x")




    root.mainloop()



