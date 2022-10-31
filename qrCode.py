from audioop import add
from optparse import Option
from tkinter import *
mainScreen = Tk()

#Widget Bar Title
mainScreen.title('PAPI Testing Page')

#Set mainScreen window size (****temporary screen size*****)
mainScreen.geometry("1024x600")


#def open():
    #dropDownLabel = Label(mainScreen, text = userSelect.get())
   # dropDownLabel.grid(row = 2, column = 2 )

#Drop down menu for candy selection
#options = [
    #'M&Ms',
    #'Skittles',
    #'Smarties',
    #'Beans',
#]

#To allow user to select an option
#userSelect = StringVar()
#userSelect.set(options[0])

#drop = OptionMenu(mainScreen, userSelect, *options)
#drop.grid(row = 1, column = 1)

#optionButtons = Button (mainScreen, text = "Select", command = open)
#optionButtons.grid(row = 1, column = 2)


#Plus/Minus Entry Options
#Setup Output of Input Value into textbox
HUIinput=Entry(mainScreen, row = 1, column = 4, columnspan = 2)

def plusMinus():
    global plus
    global minus
    current = HUIinput.get()
    HUIinput.delete (0,END)
    plus += 1
    minus -= 1

    #Creating Plus and Minus Buttons
    plusButton = Button(mainScreen, text = "+", command = HUIinput)
    minusButton = Button(mainScreen, text = "-", command = HUIinput)













mainScreen.mainloop()