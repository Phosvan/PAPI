
#include <Servo.h>                                                  // Need to add library for the servo motors 

Servo Hop1;                                                         // Designate these as servos
Servo Hop2;
Servo Hop3;
Servo Hop4;
Servo Hop5;
Servo Hop6;
Servo Hop7;
Servo Hop8;
Servo Hop9;
Servo Hop10;
Servo Hop11;
Servo Hop12;

char PiInput;                                                       // Input is expected to be a character 

void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);                                               // Start the Serial monitor on baud 9600

  Hop1.attach(2);                                                   // Set pins on Arduino for each Servo
  Hop2.attach(3);
  Hop3.attach(4);
  Hop4.attach(5);
  Hop5.attach(6);
  Hop6.attach(7);
  Hop7.attach(8);
  Hop8.attach(9);
  Hop9.attach(10);
  Hop10.attach(11);
  Hop11.attach(12);
  Hop12.attach(13);

}

void loop() {
  // put your main code here, to run repeatedly:

  while (Serial.available()){                                       // Only do this when the moitor is open
    PiInput = Serial.read();                                        // Set the value of PiInput to whatever is typed in the monitor

    if (PiInput == '1'){                                            // If one is typed, turn the servo motor 1 to dispense one pill
      Serial.println("Dispense pill 1");                            // and so on for the others
      Hop1.writeMicroseconds(1435);
      delay(460);
      Hop1.writeMicroseconds(1500);
    }
  
    else if (PiInput == '2'){
      Serial.println("Dispense pill 2");
      Hop2.writeMicroseconds(1435);
      delay(460);
      Hop2.writeMicroseconds(1500);
    }

    else if (PiInput == '3'){
      Serial.println("Dispense pill 3");
      Hop3.writeMicroseconds(1435);
      delay(460);
      Hop3.writeMicroseconds(1500);
    }

    else if (PiInput == '4'){
      Serial.println("Dispense pill 4");
      Hop4.writeMicroseconds(1435);
      delay(460);
      Hop4.writeMicroseconds(1500);
    }

    else if (PiInput == '5'){
      Serial.println("Dispense pill 5");
      Hop5.writeMicroseconds(1435);
      delay(460);
      Hop5.writeMicroseconds(1500);
    }

    else if (PiInput == '6'){
      Serial.println("Dispense pill 6");
      Hop6.writeMicroseconds(1435);
      delay(460);
      Hop6.writeMicroseconds(1500);
    }

    else if (PiInput == '7'){
      Serial.println("Dispense pill 7");
      Hop7.writeMicroseconds(1435);
      delay(460);
      Hop7.writeMicroseconds(1500);
    }

    else if (PiInput == '8'){
      Serial.println("Dispense pill 8");
      Hop8.writeMicroseconds(1435);
      delay(460);
      Hop8.writeMicroseconds(1500);
    }

    else if (PiInput == '9'){
      Serial.println("Dispense pill 9");
      Hop9.writeMicroseconds(1435);
      delay(460);
      Hop9.writeMicroseconds(1500);
    }

    else if (PiInput == 't'){
      Serial.println("Dispense pill 10");
      Hop10.writeMicroseconds(1435);
      delay(460);
      Hop10.writeMicroseconds(1500);
    }

    else if (PiInput == 'e'){
      Serial.println("Dispense pill 11");
      Hop11.writeMicroseconds(1435);
      delay(460);
      Hop11.writeMicroseconds(1500);
    }

    else if (PiInput == 't'){
      Serial.println("Dispense pill 12");
      Hop12.writeMicroseconds(1435);
      delay(460);
      Hop12.writeMicroseconds(1500);
    }

    else {                                                         // When there is no input, make sure servos are not moving 
      Hop1.writeMicroseconds(1500);
      Hop2.writeMicroseconds(1500);
      Hop3.writeMicroseconds(1500);
      Hop4.writeMicroseconds(1500);
      Hop5.writeMicroseconds(1500);
      Hop6.writeMicroseconds(1500);
      Hop7.writeMicroseconds(1500);
      Hop8.writeMicroseconds(1500);
      Hop9.writeMicroseconds(1500);
      Hop10.writeMicroseconds(1500);
      Hop11.writeMicroseconds(1500);
      Hop12.writeMicroseconds(1500);
    }
  }

}
