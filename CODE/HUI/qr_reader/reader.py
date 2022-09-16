from multiprocessing.sharedctypes import Value
from tkinter import Frame
import cv2 as cv

def detect_qr(frame):
    detectQR = cv.QRCodeDetector()
    ret, points = detectQR.detect(frame)
    return ret, points

def read_qr(frame, points):
    detect = cv.QRCodeDetector()
    value, _ = detect.decode(frame, points)

    if value == '':
        return None

    return value 

def read_main():
    while True:
        vid = cv.VideoCapture(0)
        ret, frame = vid.read()

        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        ret, points = detect_qr(frame)
        if ret:
            qr_value = read_qr(frame, points)

            if qr_value is None: continue
            else: return qr_value
            break
        
    vid.release()