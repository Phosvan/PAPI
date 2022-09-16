import tkinter as tk
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
    clean_widgets()

def createwidgets(pair):
    if len(obj) < 8:
        obj.append(WidgetSet(pair))

def clean_widgets():
    obj.pop(0).destroy()
    for widgetset in obj:
        removewidgets(widgetset)

def removewidgets(widgetset):
    slaves = widgetset.frame.winfo_children()
    for widget in slaves:
        if widget is tk.Frame:
            removewidgets(widget)
        widget.destroy()

def flatten(l):
  out = []
  for item in l:
    if isinstance(item, (list, tuple)):
      out.extend(flatten(item))
    else:
      out.append(item)
  return out

obj = []
root = tk.Tk()
def hui_main(packet):
    root.geometry("800x480")

    name_label = tk.Label(root, text=packet[0])
    name_label.pack(side="top")
    obj.append(name_label)

    for pair in packet[1::]:
        createwidgets(pair)

    string_packet = ','.join(flatten(packet))

    createWidgetButton = tk.Button(root, height=2, text="Done", command=lambda: output_data(string_packet))
    createWidgetButton.pack(side="bottom", fill="x")

    root.mainloop()



