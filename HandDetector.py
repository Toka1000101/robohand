import cv2 as cv
import mediapipe as mp
import time

capture = cv.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = capture.read()
    imgRgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    result = hands.process(imgRgb)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            # cv.putText(img, str(handLms), (10, 100), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
            for point_id, lm in enumerate(handLms.landmark):
                if point_id == 8:
                    height, witdth, _ = img.shape
                    x, y = int(lm.x * witdth), int(lm.y * height)
                    cv.circle(img, (x, y), 10, (0, 255, 0), -1)
                    cv.putText(img, str((x,y)), (10, 100), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv.imshow('Webcam', cv.flip(img, 2))
    cv.waitKey(1)


