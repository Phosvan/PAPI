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
        print(PI.scan_input_bool)
        if PI.scan_input_bool is True and PI.scan_input_data is None:
            PI.scan_input_data = PI.scan_input()
            PI.scan_input_bool = False
        
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
        print(HUI.scan_input_bool)
        if HUI.scan_input_data is None:
            HUI.show_frame('start')
            HUI.scan_input_bool = True
            HUI.update()

        if HUI.scan_input_data is not None:
            HUI.scan_input_bool = False
            HUI.show_frame('choice', HUI.scan_input_data)
            HUI.update()
        

def logic():
    PiProcess = Process(target=PiFunction)
    HuiProcess = Process(target=HuiFunction)

    PiProcess.start()
    HuiProcess.start()


if __name__ == '__main__':
    LogicController = Controller()
    logic()