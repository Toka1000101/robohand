import math
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

serial_port = '/dev/cu.usbmodem101'
ser = serial.Serial(serial_port, baudrate=9600, timeout=1)

while True:
    success, img = capture.read()
    imgRgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    result = hands.process(imgRgb)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            middle_finger_tip = handLms.landmark[mpHands.HandLandmark.MIDDLE_FINGER_TIP]
            middle_finger_mcp = handLms.landmark[mpHands.HandLandmark.MIDDLE_FINGER_MCP]
            if middle_finger_tip.y > middle_finger_mcp.y:
                msg = f"1".encode()
                ser.write(msg)
            if middle_finger_tip.y < middle_finger_mcp.y:
                msg = f"0".encode()
                ser.write(msg)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    # cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv.imshow('Webcam', img)
    cv.waitKey(1)
