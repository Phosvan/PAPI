from audioop import add
from optparse import Option
from tkinter import *
mainScreen = Tk()
###
# I was dying on the inside trying to make the other code work so here is my attempt to 
# make it not be absolute trash lol
###

#Widget Bar Title
mainScreen.title('PAPI Testing Page')
#Set mainScreen window size (****temporary screen size*****)
mainScreen.geometry("500x500")



#************OPTION ONE*******************
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
userSelect = StringVar()
userSelect.set(optionsOne[0])

drop = OptionMenu(mainScreen, userSelect, *optionsOne)
drop.grid(row = 1, column = 1)

#for amount of pills
amount = Spinbox(mainScreen, from_ = 0, to = 30)
amount.grid(row = 1, column = 10, columnspan = 1)



#***********OPTION TWO******************
optionsTwo = [
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
userSelect = StringVar()
userSelect.set(optionsTwo[0])

drop = OptionMenu(mainScreen, userSelect, *optionsTwo)
drop.grid(row = 3, column = 1)

#for amount of pills
amount = Spinbox(mainScreen, from_ = 0, to = 30)
amount.grid(row = 3, column = 10, columnspan = 1)



#************OPTION THREE****************
optionsThree = [
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
userSelect = StringVar()
userSelect.set(optionsThree[0])

drop = OptionMenu(mainScreen, userSelect, *optionsThree)
drop.grid(row = 5, column = 1)

#for amount of pills
amount = Spinbox(mainScreen, from_ = 0, to = 30)
amount.grid(row = 5, column = 10, columnspan = 1)



#*************OPTION FOUR******************
optionsFour = [
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
userSelect = StringVar()
userSelect.set(optionsFour[0])

drop = OptionMenu(mainScreen, userSelect, *optionsFour)
drop.grid(row = 7, column = 1)

#for amount of pills
amount = Spinbox(mainScreen, from_ = 0, to = 30)
amount.grid(row = 7, column = 10, columnspan = 1)



#***************OPTION FIVE***************
optionsFive = [
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
userSelect = StringVar()
userSelect.set(optionsFive[0])

drop = OptionMenu(mainScreen, userSelect, *optionsFive)
drop.grid(row = 9, column = 1)

#for amount of pills
amount = Spinbox(mainScreen, from_ = 0, to = 30)
amount.grid(row = 9, column = 10, columnspan = 1)



#************OPTION SIX*******************
optionSix = [
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
userSelect = StringVar()
userSelect.set(optionSix[0])

drop = OptionMenu(mainScreen, userSelect, *optionSix)
drop.grid(row = 11, column = 1)

#for amount of pills
amount = Spinbox(mainScreen, from_ = 0, to = 30)
amount.grid(row = 11, column = 10, columnspan = 1)



#***************OPTION SEVEN***************
optionsSeven = [
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
userSelect = StringVar()
userSelect.set(optionsSeven[0])

drop = OptionMenu(mainScreen, userSelect, *optionsSeven)
drop.grid(row = 13, column = 1)

#for amount of pills
amount = Spinbox(mainScreen, from_ = 0, to = 30)
amount.grid(row = 13, column = 10, columnspan = 1)



#***************OPTION EIGHT***************
optionsEight = [
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
userSelect = StringVar()
userSelect.set(optionsEight[0])

drop = OptionMenu(mainScreen, userSelect, *optionsEight)
drop.grid(row = 15, column = 1)

#for amount of pills
amount = Spinbox(mainScreen, from_ = 0, to = 30)
amount.grid(row = 15, column = 10, columnspan = 1)



#***************OPTION NINE***************
optionsNine = [
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
userSelect = StringVar()
userSelect.set(optionsNine[0])

drop = OptionMenu(mainScreen, userSelect, *optionsNine)
drop.grid(row = 17, column = 1)

#for amount of pills
amount = Spinbox(mainScreen, from_ = 0, to = 30)
amount.grid(row = 17, column = 10, columnspan = 1)



#***************OPTION TEN***************
optionsTen = [
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
userSelect = StringVar()
userSelect.set(optionsTen[0])

drop = OptionMenu(mainScreen, userSelect, *optionsTen)
drop.grid(row = 19, column = 1)

#for amount of pills
amount = Spinbox(mainScreen, from_ = 0, to = 30)
amount.grid(row = 19, column = 10, columnspan = 1)

mainScreen.mainloop()