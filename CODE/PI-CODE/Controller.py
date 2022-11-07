from multiprocessing import *
from ControllerClass import HuiController
from ControllerClass import PiController


def logic():

    scan_input_data = None

    HUI = HuiController()
    PI = PiController(HUI)

    while True:
        if PI.listen() == "calibrate":
            PI.speak("<confirmed>")
            while PI.listen() == "continue":
                PI.speak(PI.scan_input())
        else:
            if scan_input_data is None:
                HUI.show_frame('start')
                scan_input_data = PI.scan_input()
                print(scan_input_data)
                print("Wtf")
                HUI.update()
            
            if scan_input_data is not None:
                scan_input_data_tmp = scan_input_data.split(',')
                HUI.show_frame('choice', data=scan_input_data_tmp)

                while HUI.tmp is None:
                    HUI.update()

                if HUI.tmp == True:
                    PI.speak(scan_input_data)
                    print(PI.listen())
                    
                    HUI.tmp = None
                    scan_input_data = None

                    HUI.update()


                if HUI.tmp == False:
                    scan_input_data = None
                    HUI.tmp = None

                    HUI.update()


if __name__ == '__main__':
    logic()