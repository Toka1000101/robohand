# Robotic Hand from project inmoov - https://inmoov.fr/

Robotic hand that can open and close fingers based on hand movement in camera
It consists of 2 parts: camera frontend and arduino backend.
Python program gets landmarks of hand and sends signals to arudino. Arduino progam then opens and closes fingers accordingly.


# Hardware
All specifics of hardware and how it works can be found at inmoov website: https://inmoov.fr/hand-i2/

# Software
Python frontend:
When arduino is plugged into computer, serial_port should be change accordigly.
Python program sends signal to ardunino and notifies which fingers are closed and opened.
When showing hand to the camera result should be something like this:

![image](https://github.com/Toka1000101/robohand/assets/49341361/455b5116-dc04-4cec-a0db-445ed5ad9321)

Arduino backend:
Arduino backend receives signals from python frontend and sends signals to servos.
Servos then close or open fingers of the hand.

# How to run
1) Construct hand-i2 according to tutorial: https://inmoov.fr/hand-i2/ (All 3D parts for printing can be found in website)
2) Upload .ino code into arduino (simplest way is to do with arduino IDE)
3) configure serial_port in RoboHand.py
4) Run python file


Demo:

![robohand demo - optimized](https://github.com/Toka1000101/robohand/assets/49341361/f07188ef-4277-4731-aee9-1218e3e728ed)
