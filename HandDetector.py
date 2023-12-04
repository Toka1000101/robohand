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

serial_port = '/dev/cu.usbmodem1101'
ser = serial.Serial(serial_port, baudrate=9600, timeout=1)
msg_prev = ""


def calculate_angle(x1, y1, x2, y2):
    angle_rad = math.atan2(y2 - y1, x2 - x1)
    angle_deg = math.degrees(angle_rad)
    return angle_deg


while True:
    success, img = capture.read()
    imgRgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    result = hands.process(imgRgb)

    if result.multi_hand_landmarks:

        for handLms in result.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            # identify two ends of fingers, tips and mcps
            thumb_tip = handLms.landmark[mpHands.HandLandmark.THUMB_TIP]
            index_tip = handLms.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP]
            middle_tip = handLms.landmark[mpHands.HandLandmark.MIDDLE_FINGER_TIP]
            ring_tip = handLms.landmark[mpHands.HandLandmark.RING_FINGER_TIP]
            pinky_tip = handLms.landmark[mpHands.HandLandmark.PINKY_TIP]

            thumb_mcp = handLms.landmark[mpHands.HandLandmark.THUMB_MCP]
            index_mcp = handLms.landmark[mpHands.HandLandmark.INDEX_FINGER_MCP]
            middle_mcp = handLms.landmark[mpHands.HandLandmark.MIDDLE_FINGER_MCP]
            ring_mcp = handLms.landmark[mpHands.HandLandmark.RING_FINGER_MCP]
            pinky_mcp = handLms.landmark[mpHands.HandLandmark.PINKY_MCP]

            thumb_base = handLms.landmark[mpHands.HandLandmark.THUMB_CMC]

            tips_y = [thumb_tip.y, index_tip.y, middle_tip.y, ring_tip.y, pinky_tip.y]
            mcps_y = [thumb_mcp.y, index_mcp.y, middle_mcp.y, ring_mcp.y, pinky_mcp.y]

            msg = [0, 0, 0, 0, 0]
            for i in range(len(tips_y)):
                if i == 0:
                    angle = calculate_angle(thumb_mcp.x,
                                            thumb_mcp.y,
                                            thumb_tip.x,
                                            thumb_tip.y)

                    angle_abs = abs(angle)
                    # print(angle_abs)
                    if angle_abs > 100:
                        msg[i] = 1
                    else:
                        msg[i] = 0

                elif tips_y[i] >= mcps_y[i]:
                    msg[i] = 1
                elif tips_y[i] < mcps_y[i]:
                    msg[i] = 0

            msg_str = ''.join(str(ch) for ch in msg)

            if msg_str != msg_prev:
                print(msg_str)
                ser.write(f"{msg_str}".encode())
                msg_prev = msg_str

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(img, str(int(fps)), (10, 100), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv.imshow('Webcam', img)
    cv.waitKey(1)
