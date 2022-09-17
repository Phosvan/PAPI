import cv2 as cv

# Finds and 'annotates' qr code within frame.
def detect_qr(frame):
    detectQR = cv.QRCodeDetector()
    ret, points = detectQR.detect(frame)
    return ret, points

# Uses 'annotation' to detect and decode the qr code.
def read_qr(frame, points):
    detect = cv.QRCodeDetector()
    value, _ = detect.decode(frame, points)

    # Sometimes it reads a qr code as an empty string. Unsure why.
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
        if ret: # qr code exists
            qr_value = read_qr(frame, points)

            if qr_value is None: continue # Keep looping
            else: return qr_value
            
        
    vid.release()