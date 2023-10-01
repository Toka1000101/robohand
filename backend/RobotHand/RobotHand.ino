
#include <Servo.h>

Servo servo;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  servo.attach(8);
  servo.write(0);

}

void loop() {
  // put your main code here, to run repeatedly:
  int angle = Serial.parseInt();
  if (Serial.read() == '\n')
  Serial.println(angle);
  servo.write(angle);
}
