from qr_reader import reader
from interface import HUI


def parse_string(prescription_string):
    prescription_list = prescription_string.split(',')

    prescription_name = prescription_list.pop(0)
    prescription_pairs = [prescription_list[i:i + 2] for i in range(0, len(prescription_list), 2)]

    prescription_list = [prescription_name]
    for pair in prescription_pairs:
        prescription_list.append(pair)

        if len(prescription_list) == 9:
            break

    return prescription_list

def main():
    prescription_string = "Abigale Rhodes,Pill 1,20,Pill 1,20,Pill 1,20,Pill 1,20,Pill 1,20,Pill 1,20,Pill 1,20,Pill 1,20,Pill 1,20"
    packet = parse_string(prescription_string)
    HUI.hui_main(packet)

main()