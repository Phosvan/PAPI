from tkinter import *
from tkinter import ttk

def counterMinus():
    if counter.get() > 0:
        counter.set(counter.get()-1)

def counterPlus():
    counter.set(counter.get()+1)

def outputData():
    print(f"{text_input.get()} : {counter.get()}")

root = Tk()
root.geometry("500x500")
counter = IntVar()
input_str = StringVar()

counter_label = Label(root, textvariable=counter)
counter_label.place(x=365,y=20)

minus_button = Button(root, text="-", command=counterMinus)
minus_button.place(x=300, y=15)

plus_button = Button(root, text="+", command=counterPlus)
plus_button.place(x=400, y=15)

plus_button = Button(root, text="Done", command=outputData)
plus_button.place(x=400, y=400)

text_input = Entry(root, text="Enter A Pill")
text_input.place(x=10, y=10)

root.mainloop()





