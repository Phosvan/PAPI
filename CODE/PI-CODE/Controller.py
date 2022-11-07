from multiprocessing import *
from ControllerClass import HuiController
from ControllerClass import PiController


def logic():
    scan_input_bool = True
    listen_bool = False
    speak_bool = False
    listen_data = None
    scan_input_data = None

    HUI = HuiController()
    PI = PiController(HUI)

    while True:
        if scan_input_data is None and scan_input_bool is True:
            HUI.show_frame('start')
            scan_input_data = PI.scan_input()
            HUI.update()
        
        if scan_input_data is not None and scan_input_bool is True:
            scan_input_data_tmp = scan_input_data.split(',')
            HUI.show_frame('choice', data=scan_input_data_tmp)
            
            while HUI.tmp is None:
                HUI.update()

            if HUI.tmp == True:
                PI.speak(scan_input_data)
                HUI.update()


if __name__ == '__main__':
    logic()