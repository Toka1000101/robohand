#include <Servo.h>

Servo pinky;
Servo ring;
Servo middle;
Servo index;
Servo thumb;
Servo wrist;

byte pinkyDigitalPort = 2;
byte ringDigitalPort = 7;
byte middleDigitalPort = 6;
byte indexDigitalPort = 4;
byte thumbDigitalPort = 3;
byte wristDigitalPort = 5;

// index - 2, middle - 3, rign - 4, pinky - 6
void setupServos(byte angle) {
  pinky.attach(pinkyDigitalPort);
  ring.attach(ringDigitalPort);
  middle.attach(middleDigitalPort);
  index.attach(indexDigitalPort);
  thumb.attach(thumbDigitalPort);
  wrist.attach(wristDigitalPort);

  pinky.write(angle);
  ring.write(angle);
  middle.write(angle);
  index.write(angle);
  thumb.write(angle);
  wrist.write(angle);
}

// turns all servos from 0 to 180 at the same time
// with 1 second delay
void servosTest() {
  pinky.write(0);
  ring.write(0);
  middle.write(0);
  index.write(0);
  thumb.write(0);
  wrist.write(0);
  
  delay(5000);

  pinky.write(180);
  ring.write(180);
  middle.write(180);
  index.write(180);
  thumb.write(180);
  wrist.write(180);

  delay(5000);
}
void bendFingers() {
  pinky.write(120);
  ring.write(120);
  middle.write(120);
  index.write(120);
  thumb.write(120);
}

void expandFingers() {
  pinky.write(0);
  ring.write(0);
  middle.write(0);
  index.write(0);
  thumb.write(0);
}

void setup() {
  setupServos(0);
  Serial.begin(9600);
}


int signals[6] = {0,0,0,0,0,0};

void loop() {
  if (Serial.available()) {
    String input = "";
    while(Serial.available() == 5) {
      for(int i = 0; i < 6; i++){
        signals[i] = Serial.read() - '0';
      }
      Serial.flush();
    }


    for(int i = 0; i < 6; i++){
      Serial.print(signals[i]);
      Serial.print("-");
    }

    if(signals[0] == 1) {thumb.write(180);} else {thumb.write(0);}
    if(signals[1] == 1) {index.write(180);} else {index.write(0);}
    if(signals[2] == 1) {middle.write(180);} else {middle.write(0);}
    if(signals[3] == 1) {ring.write(180);} else {ring.write(0);}
    if(signals[4] == 1) {pinky.write(180);} else {pinky.write(0);}
    if(signals[5] == 1) {wrist.write(180);} else {wrist.write(0);}

    Serial.flush();
    Serial.println();
  }
}