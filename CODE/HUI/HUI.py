import tkinter as tk
from libs.qr_reader import reader
from libs import util
from libs.WidgetSet import WidgetSet

widget_sets = [] #TODO Remove global list and integrate into logic, class maybe?

root = tk.Tk()
root.geometry("800x480") # Raspberry Pi TouchScreen 7in Resolution

def hui_main():

    #Parsing the qr code and converting to this format to create a WidgetSet
    display_prescription(["aby", ["bofa","3"]])

    #TODO Work this logic. Need flow control.
    root.mainloop()

#TODO To be determined; how to format and send data from the HUI
def output_data(prescription):
    print(prescription)
    clean_widgets()

# Creates a widgetset object and adds to the global list.
def createwidgets(prescription_pair):
    if len(widget_sets) < 8:
        widget_sets.append(WidgetSet(prescription_pair, root))

# Destroys an entire widgetset object. calling destroy() is neccessary for the gui stuff to be removed.
def clean_widgets():

    # Helper function for clean_widgets, recursively deletes the tkinter objects within the widgetset object.
    def removewidgets(widgetset):
        slaves = widgetset.frame.winfo_children()
        for widget in slaves:
            if widget is tk.Frame:
                removewidgets(widget)
            widget.destroy()

    widget_sets.pop(0).destroy()
    for widget_set in widget_sets:
        removewidgets(widget_set)

# Temp logic on displaying a prescription.
def display_prescription(prescription):

    name_label = tk.Label(root, text=prescription[0])
    name_label.pack(side="top")
    widget_sets.append(name_label)

    for pair in prescription[1::]:
        createwidgets(pair)

    string_prescription = None #','.join(util.flatten(prescription)) #TODO Write flatten(list)

    # Temp done button for testing.
    createWidgetButton = tk.Button(root, height=2, text="Done", command=lambda: output_data(string_prescription))
    createWidgetButton.pack(side="bottom", fill="x")


hui_main()