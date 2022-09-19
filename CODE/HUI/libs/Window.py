import tkinter as tk
from libs.WidgetSet import WidgetSet

class Window:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.geometry("800x480")

    def create_WidgetSet(self, prescription_pair):
        if len(WidgetSet.sets) < 8:
            WidgetSet.sets.append((WidgetSet(prescription_pair, self.root )))

    def destroy_WidgetSets(self):
        for widget in WidgetSet.sets:
            widget.destroy()