import tkinter as tk

class WidgetSet():
    widget_sets = []
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
    # Destructor
    def destroy(self):
        self.frame.destroy()
        self.label.destroy()
        self.entry.destroy()
        self.inner_frame.destroy()