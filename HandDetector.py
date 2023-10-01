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


serial_port = '/dev/cu.usbmodem2101'
ser = serial.Serial(serial_port, baudrate=9600, timeout=1)

while True:
    success, img = capture.read()
    imgRgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    result = hands.process(imgRgb)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            index_fingertip = handLms.landmark[8]  # Tip of the index finger
            index_knuckle_middle = handLms.landmark[7]  # Middle knuckle of the index finger
            index_knuckle_base = handLms.landmark[6]  # Base knuckle of the index finger

            # Calculate the vectors from the knuckle to the fingertip
            vector1 = (index_fingertip.x - index_knuckle_middle.x, index_fingertip.y - index_knuckle_middle.y)
            vector2 = (index_knuckle_base.x - index_knuckle_middle.x, index_knuckle_base.y - index_knuckle_middle.y)

            # Calculate the angle between the two vectors
            angle = math.degrees(math.acos((vector1[0] * vector2[0] + vector1[1] * vector2[1]) /
                                           (math.sqrt(vector1[0] ** 2 + vector1[1] ** 2) *
                                            math.sqrt(vector2[0] ** 2 + vector2[1] ** 2))))
            angle_integer = int(angle)
            msg = f"{angle_integer}\n".encode()
            ser.write(msg)
            print(msg)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    # cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv.imshow('Webcam', img)
    cv.waitKey(1)


