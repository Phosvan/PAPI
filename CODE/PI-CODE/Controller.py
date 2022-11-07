from multiprocessing import *
from ControllerClass import HuiController
from ControllerClass import PiController
from ControllerClass import Controller

scan_input_bool = False
listen_bool = False
speak_bool = False
    
scan_input_data = None
listen_data = None


def PiFunction():

    global scan_input_bool
    global listen_bool
    global speak_bool
    global listen_data
    global scan_input_data

    PI = PiController()
    while True:
        print(scan_input_bool)
        if scan_input_bool is True and scan_input_data is None:
            scan_input_data = PI.scan_input()
            scan_input_bool = False
        
        # if PI.listen_bool is True:
        #     PI.listen_data = PI.listen()
        #     PI.listen_bool = False

        # if PI.speak_bool is True and PI.scan_input_data is not None:
        #     PI.speak(PI.scan_input_data)
        #     if PI.listen() == "done":
        #         PI.scan_input_data = None


def HuiFunction():

    global scan_input_bool
    global listen_bool
    global speak_bool
    global listen_data
    global scan_input_data

    HUI = HuiController()
    while True:
        if scan_input_data is None:
            HUI.show_frame('start')
            scan_input_bool = True
            print("Here")
            HUI.update()

        # if scan_input_data is not None:
        #     scan_input_bool = False
        #     HUI.show_frame('choice', scan_input_data)
        #     HUI.update()
        

def logic():
    PiProcess = Process(target=PiFunction)
    HuiProcess = Process(target=HuiFunction)

    PiProcess.start()
    HuiProcess.start()


if __name__ == '__main__':
    LogicController = Controller()
    logic()