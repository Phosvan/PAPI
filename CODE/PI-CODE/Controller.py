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
            HUI.show_frame('start')
            scan_input_data = PI.scan_input()
            PI.speak('y')
            HUI.update()
        
        # elif scan_input_data == "Manual":
            
            # HUI.show_frame('manual')
            # while HUI.mm_send_bool is None:
            #     HUI.update()

            # if HUI.mm_send_bool:
            #     simulated_data = ['simulated']
            #     for option_object in HUI.frames['manual'].entrys:
            #         simulated_data.append(option_object.drop_menu.get())
            #         simulated_data.append(option_object.amount.get())
            #         HUI.update()

            #     simulated_data = ','.join(simulated_data)
            #     PI.speak(simulated_data)
            #     while PI.listen() != "done":
            #         HUI.update()
            #         HUI.mm_bool = None
            #         HUI.mm_send_bool = None
            #         scan_input_data = None
            
            # else:
            #     scan_input_data = None
            #     HUI.mm_bool = None
            #     HUI.mm_send_bool = None
            #     HUI.update()

        if scan_input_data is not None:
            scan_input_data_tmp = scan_input_data.split(',')
            HUI.show_frame('choice', data=scan_input_data_tmp)

            while HUI.tmp is None:
                HUI.update()

            if HUI.tmp == True:
                PI.speak('y')
                # while PI.listen() != "done":
                    print("done")
                    HUI.update()
                
                HUI.tmp = None
                scan_input_data = None

                HUI.update()


            else:
                scan_input_data = None
                HUI.tmp = None

                HUI.update()


if __name__ == '__main__':
    logic()