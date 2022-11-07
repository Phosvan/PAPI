from audioop import add
from optparse import Option
from tkinter import *
mainScreen = Tk()

#Widget Bar Title
mainScreen.title('PAPI Testing Page')

#Set mainScreen window size (****temporary screen size*****)
mainScreen.geometry("1024x600")

#*******HOPPER ONE**********
#Drop down menu for candy selection: (1 | 10)
optionsOne = [
    'hop1',
    'hop2',
    'hop3',
    'hop4',
    'hop5',
    'hop6',
    'hop7',
    'hop8',
    'hop9',
    'hop10'
]

#To allow user to select an option
userSelect = StringVar()
userSelect.set(optionsOne[0])

drop = OptionMenu(mainScreen, userSelect, *optionsOne)
drop.grid(row = 1, column = 1)


#Plus/Minus Entry Options
#Setup Output of Input Value into textbox
plus = Entry(mainScreen)
plus.grid(row = 1, column = 4, columnspan = 1)

minus = Entry(mainScreen)
minus.grid(row = 1, column = 4, columnspan = 1)

current = plus.get







def plus():
    global plus
    current = userInput.get()
    userInput.delete (0, END)
    plus += 1

    plusButton = Label(plus)
    plusButton = Button(mainScreen, text = "+")
    plusButton.grid(row = 2, column = 6)


def minus():
    global minus
    current = userInput.get()
    userInput.delete (0, END)
    minus -= 1
    minusButton = Button(mainScreen, text = "-")
    minusButton.grid(row = 1, column = 3)














mainScreen.mainloop()