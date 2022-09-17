import tkinter as tk

class WidgetSet():
    def __init__(self, pair, root) -> None:
        self.root = root
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
        
    # Unneccessary since lack of changing IntVar labels. 
    # def Minus(self):
    #     if self.cnt.get() > 0:
    #         self.cnt.set(self.cnt.get()-1)

    # def Plus(self):
    #     if self.cnt.get() < 99:
    #         self.cnt.set(self.cnt.get()+1)