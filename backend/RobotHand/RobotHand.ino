#include <Servo.h>

Servo pinky;
Servo ring;
Servo middle;
Servo index;
Servo thumb;
Servo wrist;

byte pinkyDigitalPort = 7;
byte ringDigitalPort = 6;
byte middleDigitalPort = 5;
byte indexDigitalPort = 4;
byte thumbDigitalPort = 3;
byte wristDigitalPort = 2;

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
  
  delay(1000);

  pinky.write(180);
  ring.write(180);
  middle.write(180);
  index.write(180);
  thumb.write(180);
  wrist.write(180);

  delay(1000);
}

void setup() {
  setupServos(0);
}

void loop() {
  // servosTest();

}