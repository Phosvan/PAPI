//Houseburnerdowner code

#include <Servo.h> 

Servo myservo;  // create servo object to control a servo 
 
int Relaypin = 8; // Define input pin for relay
int servopin = 11;
int pinButton = A0;

int servohomepos = 1000; //in microseconds
int servopresspos = 2000; //in microseconds

int heaterstartuptime = 6000; //in microseconds
int heatercooldowntime = 1000; //in microseconds
int presstime = 5000; 

class MakePackage{



  public:
    void do_something(){
      digitalWrite(Relaypin, LOW); //give the wire power
      delay(heaterstartuptime); // heaterwire heatup time

      myservo.writeMicroseconds(servopresspos); //set servo to press position (ms = height)
      delay(presstime); //this determimes how long press is pressing (time)

      myservo.writeMicroseconds(servohomepos); //return servo to resting positiion
      digitalWrite(Relaypin, HIGH); //turn off wire

  }
};

MakePackage packg = MakePackage();

void setup() 
{  

  myservo.attach(servopin);  // attaches the servo on pin 9 to the servo object 
  pinMode(Relaypin, OUTPUT); // realy pin
  digitalWrite(Relaypin, HIGH); //give the wire power
  myservo.writeMicroseconds(servohomepos);

} 
 
 
void loop() 
{ 
  if (int stateButton = digitalRead(pinButton)){

    packg.do_something();
    
  }
} 