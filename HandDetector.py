import cv2 as cv
import mediapipe as mp
import time
import serial

capture = cv.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0


serial_port = '/dev/cu.usbmodem2101'
ser = serial.Serial(serial_port, baudrate=9600, timeout=1)

while True:
    success, img = capture.read()
    imgRgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    result = hands.process(imgRgb)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            index_finger_tip = handLms.landmark[8]
            index_finger_y = index_finger_tip.y
            if index_finger_y < handLms.landmark[7].y:
                cv.putText(img, "Index Finger Up", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                ser.write("U".encode())
            else:
                cv.putText(img, "Index Finger Down", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                ser.write("D".encode())

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv.imshow('Webcam', img)
    cv.waitKey(1)


