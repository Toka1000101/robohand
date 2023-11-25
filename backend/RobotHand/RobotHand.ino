#include <Servo.h>

Servo pinky;
Servo ring;
Servo middle;
Servo index;
Servo thumb;
Servo wrist;

byte pinkyDigitalPort = 4;
byte ringDigitalPort = 3;
byte middleDigitalPort = 2;
byte indexDigitalPort = 5;
byte thumbDigitalPort = 6;
byte wristDigitalPort = 7;

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

void loop() {
  
  if(Serial.available() > 0){
    char msg = Serial.read();

    if(msg == '1') {
      ring.write(170);
    } else if (msg == '0'){
      ring.write(0);
    }
  }

}