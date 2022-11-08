from multiprocessing import *
from ControllerClass import HuiController
from ControllerClass import PiController


def logic():

    scan_input_data = None

    HUI = HuiController()
    PI = PiController(HUI)

    while True:
        # if PI.listen() == "calibrate":
        #     PI.speak("<confirmed>")
        #     while PI.listen() == "continue":
        #         PI.speak(PI.scan_input())
        # else:
        if scan_input_data is None:
            print(1)
            print(scan_input_data)
            HUI.show_frame('start')
            scan_input_data = PI.scan_input()
            HUI.update()
        
        if scan_input_data is not None:
            print(2)
            print(scan_input_data)
            scan_input_data_tmp = scan_input_data.split(',')
            HUI.show_frame('choice', data=scan_input_data_tmp)

            while HUI.tmp is None:
                print(3)
                print(scan_input_data)
                HUI.update()

            if HUI.tmp == True:
                print(4)
                print(scan_input_data)
                PI.speak(scan_input_data)
                print(PI.listen())
                
                HUI.tmp = None
                scan_input_data = None

                HUI.update()


            if HUI.tmp == False:
                print(5)
                scan_input_data = None
                HUI.tmp = None

                HUI.update()


if __name__ == '__main__':
    logic()