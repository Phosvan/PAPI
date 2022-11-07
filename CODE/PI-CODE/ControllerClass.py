import tkinter as tk
from tkinter import font as tkfont
import cv2 as cv
import serial
from pyzbar.pyzbar import decode

class Controller:
    scan_input_bool = False
    listen_bool = False
    speak_bool = False
    
    scan_input_data = None
    listen_data = None


    def __init__(self) -> None:
        pass


class PiController(Controller):
    def __init__(self):
        self.listening = False
        self.debug = True
        self.startMarker = '<'
        self.endMarker = '>'
        self.dataStarted = False
        self.dataBuf = ""
        self.messageComplete = False
        self.vid = cv.VideoCapture(0)
        self.serialPort = None
        self.parse_file()
    
    def parse_file(self):
        self.setupSerial("9600","/dev/ttyACM0")
        
    def setupSerial(self, baudRate, serialPortName):
        self.serialPort = serial.Serial(port= serialPortName, baudrate = baudRate, timeout=0, rtscts=True)

        print("Serial port " + serialPortName + " opened  Baudrate " + str(baudRate))
        self.waitForArduino()

    def sendToArduino(self, stringToSend):
        stringWithMarkers = (self.startMarker)
        stringWithMarkers += stringToSend
        stringWithMarkers += (self.endMarker)

        self.serialPort.write(stringWithMarkers.encode('utf-8')) # encode needed for Python3
       
    def recvLikeArduino(self):
        if self.serialPort.inWaiting() > 0 and self.messageComplete == False or self.listening is True:
            x = self.serialPort.read().decode("utf-8") # decode needed for Python3
        
            if self.dataStarted == True:
                if x != self.endMarker:
                    self.dataBuf = self.dataBuf + x
                else:
                    self.dataStarted = False
                    self.messageComplete = True
            elif x == self.startMarker:
                self.dataBuf = ''
                self.dataStarted = True
    
        if (self.messageComplete == True):
            self.messageComplete = False
            return self.dataBuf
        else:
            return "XXX" 

    def waitForArduino(self):
        print("Waiting for Arduino to reset")
     
        msg = ""
        while msg.find("Arduino is ready") == -1:
            msg = self.recvLikeArduino()
            if not (msg == 'XXX'): 
                print(msg)

    def read_qr(self, frame):
        value = decode(frame)
        if len(value) == 0:
            return None

        return value[0].data.decode("utf-8") 

    def scan_input(self):
        if self.debug:
            print("Camera On")
        while True:
            ret, frame = self.vid.read()
            if ret == True:
                qr_value = self.read_qr(frame)

            if qr_value is None: continue
            else: return qr_value

    def speak(self, qr_value):
        self.sendToArduino(qr_value)

    def listen(self):
        while True:
            arduinoReply = self.recvLikeArduino()
            if not (arduinoReply == 'XXX'):
                return arduinoReply
        

class HuiController(tk.Tk, Controller):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        #self.frames['start'] = start(container=self.container, container=self)

        for F in (start, twochoice, mm):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column= 0, sticky= "nsew")

        self.show_frame("start")

    
     def show_frame(self, page_name, data =None):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

       # if page_name == 'twochoice':
        #  frame.tkraise()
        #else:
         #   frame = self.frames[page_name]
          #  frame.tkraise()

        #def create_twochoice(self, page_name, data):
         #self.frames[page_name] = twochoice(parent=self.container, controller=self)
          
class start(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg= "#d459de")
        self.controller = controller
        label = tk.Label (self, text= "Welcome to PAPI, Please Scan QR", width= 20, height= 5, font= ("Comic Sans Ms",50), bg= "#d459de")    
        controller.attributes('-fullscreen', True)
        label.pack(side="top", fill= "x", pady=10)   

        button1 = tk.Button (self, text= "Go to ID",
        command= lambda: controller.show_frame("twochoice"))

        button1.pack(side="bottom", fill= "x",pady=10) 


#class twochoice(tk.Frame):
     #def __init__(self, parent, controller):
        #tk.Frame.__init__(self, parent)
        #self.controller = controller
        #label1 = tk.Label(self, text= "ID#:")
        #label1.pack(side= "top", fill= "x", pady=10)
        #Label2 = tk.Label(self, text= "Name Variable Here")
        #Label2.pack(side= "top", fill= "x", pady=10)
        #button1 = tk.Button(self, text= "Correct Information",
        #command= lambda: controller.show_frame("start"))
        #button1.pack()
        #button2 = tk.Button(self, text= "Incorrect Information",
        #command= lambda: controller.show_frame("start"))
        #button2.pack()

class twochoice(tk.Frame):
     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg= "#d459de")
        self.controller = controller
        label1 = tk.Label(self, text= "ID#:", bg= "#d459de", font= ("Calibri",50), height= 1)
        label1.pack(side= "top", fill= "x", pady=5)
        Label2 = tk.Label(self, text= "Name Variable Here",bg= "#d459de", font= ("Calibri", 50), height= 1)
        Label2.pack(side= "top", fill= "x", pady=5)
        button1 = tk.Button(self, text= "Correct Information", font= ("Copper Black", 20), fg= "green",
        command= lambda: controller.show_frame("start"))
        button1.pack(side= "bottom", fill= "x", pady=5)
        button2 = tk.Button(self, text= "Incorrect Information", font= ("Copper Black", 20), fg= "red",
        command= lambda: controller.show_frame("start"))
        button2.pack(side= "bottom", fill= "x", pady=5)
        button3 = tk.Button(self, text= "Manual Entry Mode", font=("lato",20),
        command= lambda: controller.show_frame("mm"))
        button3.pack(side= "bottom", fill= "x", pady=5)


class yes(tk.Tk):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
     
class mm(tk.Frame):
     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg= "#d459de")
        self.controller = controller
        
        #label1 = tk.Label
#      def __init__(self, *args, **kwargs):
#         tk.Tk.__init__(self, *args, **kwargs)
        
#         container = tk.Frame(self)
#         container.pack(side="top", fill="both", expand=True)
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)

#         self.frames = {}
        
#         self.frames['start'] = start(parent=container, controller=self)
    
#      def show_frame(self, page_name, data = None):
#         '''Show a frame for the given page name'''
#         frame = self.frames[page_name]
#         frame.tkraise()
    
#      def flip_speak():
#         Controller.speak_bool = True

#      def set_none():
#         Controller.scan_input_data = None


#        # if page_name == 'twochoice':
#         #  frame.tkraise()
#         #else:
#          #   frame = self.frames[page_name]
#           #  frame.tkraise()

#         #def create_twochoice(self, page_name, data):
#          #self.frames[page_name] = twochoice(parent=self.container, controller=self)
          
# class start(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent, bg= "#d459de")
#         self.controller = controller
#         label = tk.Label (self, text= "Welcome to PAPI, Please Scan QR", width= 20, height= 5, font= ("Comic Sans Ms",50), bg= "#d459de")    
#         controller.attributes('-fullscreen', True)
#         label.pack(side="top", fill= "x", pady=10)   

#         button1 = tk.Button (self, text= "Go to ID",
#         command= lambda: controller.show_frame("twochoice"))

#         button1.pack(side="bottom", fill= "x",pady=10) 


# class choice(tk.Frame):
#      def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent, bg= "#d459de")
#         self.controller = controller
#         label1 = tk.Label(self, text= "ID#:", bg= "#d459de", font= ("Calibri",50), height= 1)
#         label1.pack(side= "top", fill= "x", pady=5)

#         Label2 = tk.Label(self, text= "Name Variable Here",bg= "#d459de", font= ("Calibri", 50), height= 1)
#         Label2.pack(side= "top", fill= "x", pady=5)

#         button1 = tk.Button(self, text= "Correct Information", font= ("Copper Black", 20), fg= "green",
#         command= lambda: controller.show_frame("start"))
#         button1.pack(side= "bottom", fill= "x", pady=5)

#         button2 = tk.Button(self, text= "Incorrect Information", font= ("Copper Black", 20), fg= "red",
#         command= lambda: controller.show_frame("start"))
#         button2.pack(side= "bottom", fill= "x", pady=5)

#         button3 = tk.Button(self, text= "Manual Entry Mode", font=("lato",20),
#         command= lambda: controller.show_frame("mm"))
#         button3.pack(side= "bottom", fill= "x", pady=5)


# class yes(tk.Tk):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
     

# class mm(tk.Frame):
#      def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent, bg= "#d459de")
#         self.controller = controller
#         #label1 = tk.Label
