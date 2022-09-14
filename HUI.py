import tkinter as tk

class WidgetSet():
    def __init__(self) -> None:
        self.cnt = tk.IntVar()

        self.frame = tk.Frame(root,borderwidth=0, relief="groove")
        self.frame.pack(side="top", fill="x")

        self.entry = tk.Entry(self.frame ,width=30, font=('Arial 16'), bg="white")
        self.entry.pack(side="left", padx=(100,0))

        self.inner_frame = tk.Frame(self.frame, borderwidth=0, relief="groove")
        self.inner_frame.pack(side="right", fill="x")
        
        self.button_minus = tk.Button(self.inner_frame, width=2, height= 2, text="-", command=self.Minus)
        self.button_minus.pack(side="left", )

        self.label = tk.Label(self.inner_frame, width=5, textvariable=self.cnt)
        self.label.pack(side="left")

        self.button_plus = tk.Button(self.inner_frame, width=2, height= 2, text="+", command=self.Plus)
        self.button_plus.pack(side="left", padx=(0,175))

    def Minus(self):
        if self.cnt.get() > 0:
            self.cnt.set(self.cnt.get()-1)

    def Plus(self):
        if self.cnt.get() < 99:
            self.cnt.set(self.cnt.get()+1)

root = tk.Tk()
root.geometry("800x480")

obj=[WidgetSet()]

def output_data():
    for wSet in obj:
        print(f"{wSet.entry.get()},{wSet.cnt.get()}")

def createwidgets():
    if len(obj) < 8:
        obj.append(WidgetSet())

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


createWidgetButton = tk.Button(root, height=2, text="Done", command=output_data)
createWidgetButton.pack(side="bottom", fill="x")

createWidgetButton = tk.Button(root, height=2, text="Less", command=removewidgets)
createWidgetButton.pack(side="bottom", fill="x")

createWidgetButton = tk.Button(root, height=2, text="More", command=createwidgets)
createWidgetButton.pack(side="bottom", fill="x")




root.mainloop()



