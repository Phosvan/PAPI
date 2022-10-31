from tkinter import *
mainScreen = Tk()

#Widget Bar Title
mainScreen.title('PAPI Final Product Page')

#Set mainScreen window size (****temporary screen size*****)
mainScreen.geometry("500x500")

#Output Green and Red Clicking Symbols

#Main Intro Question that will Output onto screen after barcode is scanned
introQuestion = Label(mainScreen, text = "Hello (last, first), #ORDERNUMBER :")
#Indicating where location is on grid(aesthetic purposes)
introQuestion.grid(row=1, column=1)

introQuestionTwo = Label(mainScreen, text = "Proceed to Fill?")
introQuestionTwo.grid(row=1, column=2)

#defining function of Green Button
def greenButton():
    greenLabel = Label(mainScreen, text = "Proceeding to Fill...")
    greenLabel.grid(row=4, column=1)

greenButton = Button(mainScreen, text = "YES", command=greenButton, fg  ='#3EF928')
greenButton.grid(row=3, column=3)


#defining function of Red Button
def redButton():
    redLabel = Label(mainScreen, text = "Order Cancelled" )
    redLabel.grid(row=4, column=1)

redButton = Button(mainScreen, text= "NO", command=redButton, fg ='#F92828')
redButton.grid(row=3, column=2)


#end program
mainScreen.mainloop()