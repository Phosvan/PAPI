#include <Servo.h>
#define P 53
#define M (int)pow(9, 9) + 9
#define charSize 64
#define ir_digital 16
#define ir_drop -100
#define turnSpeed 1300                                             
#define turnStop 1500
#define stepsPerRevolution 500



class IrSensor{
  public:
    uint8_t pin;
    int a,b,c;

    void set_pin(uint8_t pin){
      this->pin = pin; 
      this->calc_a();
      this->calc_b();
      this->calc_c();
    }
    void calc_a(){
      this->a = analogRead(this->pin);
    } 
    void calc_b(){
      this->b = analogRead(this->pin);
    }  
    void calc_c(){
      this->c = this->a - this->b;
    }     
};

class Hopper{
  public:
    Servo srvo;
    IrSensor ir;
    int qr_hash;
    int hop_name_hash;
    
    bool does_exist;

    void set_Hopper(Servo srvo, int pin, uint8_t ir_pin, char hop_name[]){
      this->srvo = srvo;      
      this->srvo.attach(pin);
      this->srvo.writeMicroseconds(turnStop);

      this->ir.set_pin(ir_pin);

      this->hop_name_hash = this->string_hash(hop_name);      
    }

    void set_qr(char qr[]){
      this->qr_hash = this->string_hash(qr);
    }

    /**
    This only works with lowercase letters.
    **/
    static int string_hash(char word[]) {
      int sum = 0;
      int p_pow = 0;
      for (int i = 0; word[i] != '\0'; i++){
        sum += ((word[i] - 'a' + 1) * p_pow) % M;
        p_pow = (p_pow * P) % M;
      }
      return sum;
    }
    
    drop_pills(int amount){
      int internal_count = 0;
      bool reverse_direction = false;
      bool count = true;
      while (amount > 0){
        if (this->ir.c > ir_drop){
          count = true;
        }

        if (internal_count % 5000 > 2500){
          reverse_direction = true;
        }

        else{
          reverse_direction = false;
        }

        if (reverse_direction){
          this->srvo.writeMicroseconds(turnSpeed+400);
        }
        else{
          this->srvo.writeMicroseconds(turnSpeed);
        }
        digitalWrite(ir_digital,HIGH);    // Turning ON LED
        delayMicroseconds(500);  //wait
        this->ir.calc_a();        //take reading from photodiode(pin A3) :noise+signal
        digitalWrite(ir_digital,LOW);     //turn Off LED
        delayMicroseconds(500);  //wait
        this->ir.calc_b();      // again take reading from photodiode :noise
        this->ir.calc_c();   

        // Serial.println(this->ir.c);

        if (this->ir.c < ir_drop && count == true){
          count = false;
          internal_count == 0;
          amount--;        
        }
        internal_count++;
      }
      this->srvo.writeMicroseconds(turnStop);
    }
};

int hop_hashes[10] = {
  Hopper::string_hash("hop1"),
  Hopper::string_hash("hop2"),
  Hopper::string_hash("hop3"),
  Hopper::string_hash("hop4"),
  Hopper::string_hash("hop5"),
  Hopper::string_hash("hop6"),
  Hopper::string_hash("hop7"),
  Hopper::string_hash("hop8"),
  Hopper::string_hash("hop9"),
  Hopper::string_hash("hop10")
  };

Hopper hoppers[10] = {
  Hopper(),
  Hopper(),
  Hopper(),
  Hopper(),
  Hopper(),
  Hopper(),
  Hopper(),
  Hopper(),
  Hopper(),
  Hopper()
};

Servo gate;
// Yellow step, Green direct

char serialRXArray[charSize] = { 0 }; //Initialize a char array of size charSize
char parsedRXArray[12][64] = { 0 };
int parsed_size = 1; // Due to the way parsing is done.
int hashedHopperQRs[10] = { 0 };
int hash_size = 0;

bool serialReceived = false; //Do not adjust, flag used in processing logic
bool serialParsed = false; // Sets after the RXArray get's parsed.
bool parsedHashed = false; // Sets after the parsedRXArray gets hashed.
bool pills_dispensed = false;

bool manual_mode = false;
char manual_hash[] = "simulated";

bool debug = false; // Prints shit to the pi for viewing
bool check;

bool calibration = true;

const int hopperStepPin = 2;
const int hopperDirPin = 14;

const int wrapStepPin = 13;
const int wrapDirPin = 15;


bool dispensed = false;

char yes_str[] = "start";


//===============

void setup() {
  pinMode(16, OUTPUT);
  pinMode(hopperDirPin, OUTPUT);
  pinMode(hopperStepPin, OUTPUT);
  pinMode(wrapStepPin, OUTPUT);
  pinMode(wrapDirPin, OUTPUT);

  gate.attach(44);

  Serial.begin(9600);
  Serial.println("<Arduino is ready>");

  char hop1[]  = "hopone";
  char hop2[]  = "hoptwo";
  char hop3[]  = "hopthree";
  char hop4[]  = "hopfour";
  char hop5[]  = "hopfive";
  char hop6[]  = "hopsix";
  char hop7[]  = "hopseven";
  char hop8[]  = "hopeight";
  char hop9[]  = "hopnine";
  char hop10[]  = "hopten";

  hoppers[0].set_Hopper(Servo(), 6, A4, hop1);
  hoppers[1].set_Hopper(Servo(), 11, A9, hop2);
  hoppers[2].set_Hopper(Servo(), 5, A2, hop3);
  hoppers[3].set_Hopper(Servo(), 10, A0, hop4);
  hoppers[4].set_Hopper(Servo(), 4, A3, hop5);
  hoppers[5].set_Hopper(Servo(), 9, A1, hop6);
  hoppers[6].set_Hopper(Servo(), 3, A5, hop7);
  hoppers[7].set_Hopper(Servo(), 8, A7, hop8);
  hoppers[8].set_Hopper(Servo(), 12, A6, hop9);
  hoppers[9].set_Hopper(Servo(), 7, A8, hop10);
  

  char gel_str[]  = "gel";
  char gelone_str[]  = "gelone";
  char jellybean_str[]  = "jellybean";
  char jellybeanone_str[]  = "jellybeanone";
  char mandm_str[]  = "mandm";
  char mandmone_str[]  = "mandmone";
  char skittle_str[]  = "skittle";
  char skittleone_str[]  = "skittleone";
  char tiktak_str[]  = "tiktak";
  char tiktakone_str[]  = "tiktakone";

  hoppers[0].set_qr(gel_str);
  hoppers[1].set_qr(gelone_str);
  hoppers[2].set_qr(jellybean_str);
  hoppers[3].set_qr(jellybeanone_str);
  hoppers[4].set_qr(mandm_str);
  hoppers[5].set_qr(mandmone_str);
  hoppers[6].set_qr(skittle_str);
  hoppers[7].set_qr(skittleone_str);
  hoppers[8].set_qr(tiktak_str);
  hoppers[9].set_qr(tiktakone_str);

  check = true;
  digitalWrite(hopperDirPin, HIGH);
  digitalWrite(wrapDirPin, HIGH);
}

//===============

void loop(){
  // if (calibration){
  //   if (!calibrated){
  //   calibrate();
  //   }
  //   serialRead();
  //   serialParse();
  //   // check_simulated();
  //   hash_hoppers();
  //   dispense_pills();
  //   gather_pills();

  //   pull_package();
    
  //   // package();
  //   // finish_package();
  //   // delayMicroseconds(20000);
  //   calibration = false;
    
  // }

  serialRead();
  serialParse();

  if (serialReceived){
    if (Hopper::string_hash(serialRXArray) == Hopper::string_hash(yes_str)){
        hoppers[4].drop_pills(2);
        hoppers[6].drop_pills(3);
        done();
    }
  }
  // // check_simulated();
  // hash_hoppers();
  // dispense_pills();
  // // gather_pills();
  // // pull_package();
  // // package();
  // // finish_package();
  // // delaymicroseconds(15000);
  // replyToPython();
}

// Printer is pin 33
//===============

void calibrate(){
  // Spin motor slowly
  digitalWrite(hopperDirPin, HIGH);   
  for (int i = 0; i < 1; i++){
    
    for(int x = 0; x < 150; x++)
    {
      digitalWrite(hopperStepPin, HIGH);
      delayMicroseconds(1000);
      digitalWrite(hopperStepPin, LOW);
      delayMicroseconds(1000);
    }
    delay(2000); // Wait a second   
  }
  
  for (int i = 0; i < 4; i++){
    
    for(int x = 0; x < 1000; x++)
    {
      digitalWrite(hopperStepPin, HIGH);
      delayMicroseconds(1000);
      digitalWrite(hopperStepPin, LOW);
      delayMicroseconds(1000);
    }
    delay(2000); // Wait a second    
  }
  digitalWrite(hopperDirPin, LOW);    
  for(int x = 0; x < 4220; x++)
  {
    digitalWrite(hopperStepPin, HIGH);
    delayMicroseconds(1000);
    digitalWrite(hopperStepPin, LOW);
    delayMicroseconds(1000);
  }

    // digitalWrite(hopperDirPin, HIGH);
  digitalWrite(hopperDirPin, HIGH);
}

void gather_pills(){
  digitalWrite(wrapDirPin, LOW);
  gate.write(170);
  for(int x = 0; x < 17350; x++)
  {
    digitalWrite(wrapStepPin, HIGH);
    delayMicroseconds(500);
    digitalWrite(wrapStepPin, LOW);
    delayMicroseconds(500);
  }
  gate.write(90);
  delay(1000);
}
//===============

void serialRead() { //Based on code from: https://forum.arduino.cc/index.php?topic=288234.0
  static bool serialRXInProg = false;
  static byte rxCharIndex = 0; //Initialize a byte with value zero as a pointer to the place in array to move data
  char startMarker = '<'; //All messages must begin with this. If not, it will not be read
  char endMarker = '>'; //End messages with this so the char array gets properly terminated
  char rc; //Used to hold one char from the Serial buffer until it is loaded into the array
  while (Serial.available() && serialReceived == false) { //serialReceived is initialized before first run!
    rc = Serial.read(); //Load next char in line to char rc
    //Serial.print(rc);
    if (serialRXInProg == true) {
      if (rc != endMarker) { //if the received char is NOT the endMarker
        serialRXArray[rxCharIndex] = rc; //Set serialRXArray @ location rxCharIndex to the char in rc
        rxCharIndex++; //Increment rxCharIndex in preparation for the next char 
      }
      else {
        serialRXArray[rxCharIndex] = '\0'; //Our last RX'd char was endMarker. Terminate char array
        serialRXInProg = false; //Done RX'ing. Set bool to false
        rxCharIndex = 0; //Reset rxCharIndex (Technically not necessary due to declaration at beginning of this routine)
        serialReceived = true; //We have a full char array. Prep for Logic() and Reply()

      }
    }
    
    if (rc == startMarker) { //This needs to go at the end so a startMarker doesn't waste space in serialRXArray
      serialRXInProg = true;
    }
    
  }
}

//===============

void serialParse(){
    byte upper_ptr = 0; // Indicative of position in first dimension
    byte lower_ptr = 0; // Indicative of position in second dimension
    byte i = 0;
    if (serialReceived){
      for (i = 0; serialRXArray[i] != '\0'; i++){
        if (serialRXArray[i] == ','){
            parsedRXArray[upper_ptr++][lower_ptr] = '\0';
            parsed_size++;
            lower_ptr = 0;
            continue;
        }
        parsedRXArray[upper_ptr][lower_ptr] = serialRXArray[i];
        lower_ptr++;
      }
      serialParsed = true;
    }
}

//===============

void check_simulated(){
  if (serialParsed){
    if (Hopper::string_hash(parsedRXArray[0]) == Hopper::string_hash(manual_hash)){
      manual_mode = true;
    }
  }
}

//===============

void hash_hoppers(){
  byte hash_ptr = 0;
  byte parsed_ptr = 3;
  if (serialParsed) {
    for (int i = parsed_ptr; parsed_ptr < parsed_size-1; i++) {
      hashedHopperQRs[hash_ptr++] = Hopper::string_hash(parsedRXArray[parsed_ptr]);
      hashedHopperQRs[hash_ptr++] = atoi(parsedRXArray[parsed_ptr+1]);
      hash_size+=2;
      parsed_ptr+=2;    
    }
    parsedHashed = true;
  }
  // else if (serialParsed && manual_mode){
  //   for (int i = parsed_ptr-2; parsed_ptr < parsed_size-1; i++) {
  //     hashedHopperQRs[hash_ptr++] = Hopper::string_hash(parsedRXArray[parsed_ptr]);
  //     hashedHopperQRs[hash_ptr++] = atoi(parsedRXArray[parsed_ptr+1]);
  //     hash_size+=2;
  //     parsed_ptr+=2;    
  //   }
  //   parsedHashed=true;
  // }
}

//===============

void dispense_pills(){
  byte dispense_ptr = 0;
  
  if (parsedHashed){
    while (dispense_ptr < hash_size-1){
      if (hashedHopperQRs[dispense_ptr] == hoppers[0].qr_hash){
        hoppers[0].drop_pills(hashedHopperQRs[dispense_ptr+1]);
        dispense_ptr+=2;       
      }

      else if(hashedHopperQRs[dispense_ptr] == hoppers[1].qr_hash){
        hoppers[1].drop_pills(hashedHopperQRs[dispense_ptr+1]);
        dispense_ptr+=2;       
      }

      else if(hashedHopperQRs[dispense_ptr] == hoppers[2].qr_hash){
        hoppers[2].drop_pills(hashedHopperQRs[dispense_ptr+1]);
        dispense_ptr+=2;       
      }

      else if(hashedHopperQRs[dispense_ptr] == hoppers[3].qr_hash){
        hoppers[3].drop_pills(hashedHopperQRs[dispense_ptr+1]);
        dispense_ptr+=2;       
      }

      else if(hashedHopperQRs[dispense_ptr] == hoppers[4].qr_hash){
        hoppers[4].drop_pills(hashedHopperQRs[dispense_ptr+1]);
        dispense_ptr+=2;       
      }
      
      else if(hashedHopperQRs[dispense_ptr] == hoppers[5].qr_hash){
        hoppers[5].drop_pills(hashedHopperQRs[dispense_ptr+1]);
        dispense_ptr+=2;       
      }

      else if(hashedHopperQRs[dispense_ptr] == hoppers[6].qr_hash){
        hoppers[6].drop_pills(hashedHopperQRs[dispense_ptr+1]);
        dispense_ptr+=2;       
      }

      else if(hashedHopperQRs[dispense_ptr] == hoppers[7].qr_hash){
        hoppers[7].drop_pills(hashedHopperQRs[dispense_ptr+1]);
        dispense_ptr+=2;       
      }

      else if(hashedHopperQRs[dispense_ptr] == hoppers[8].qr_hash){
        hoppers[8].drop_pills(hashedHopperQRs[dispense_ptr+1]);
        dispense_ptr+=2;       
      }

      else if(hashedHopperQRs[dispense_ptr] == hoppers[9].qr_hash){
        hoppers[9].drop_pills(hashedHopperQRs[dispense_ptr+1]);
        dispense_ptr+=2;       
      }
    }
    dispensed = true;
  }
  // else if (parsedHashed && manual_mode){
  //   while (dispense_ptr < hash_size-1){
  //     if (hashedHopperQRs[dispense_ptr] == hoppers[0].hop_name_hash){
  //       hoppers[0].drop_pills(hashedHopperQRs[dispense_ptr+1]);
  //       dispense_ptr+=2;       
  //     }

  //     else if(hashedHopperQRs[dispense_ptr] == hoppers[1].hop_name_hash){
  //       hoppers[1].drop_pills(hashedHopperQRs[dispense_ptr+1]);
  //       dispense_ptr+=2;       
  //     }

  //     else if(hashedHopperQRs[dispense_ptr] == hoppers[2].hop_name_hash){
  //       hoppers[2].drop_pills(hashedHopperQRs[dispense_ptr+1]);
  //       dispense_ptr+=2;       
  //     }

  //     else if(hashedHopperQRs[dispense_ptr] == hoppers[3].hop_name_hash){
  //       hoppers[3].drop_pills(hashedHopperQRs[dispense_ptr+1]);
  //       dispense_ptr+=2;       
  //     }

    //   else if(hashedHopperQRs[dispense_ptr] == hoppers[4].hop_name_hash){
    //     hoppers[4].drop_pills(hashedHopperQRs[dispense_ptr+1]);
    //     dispense_ptr+=2;       
    //   }
      
    //   else if(hashedHopperQRs[dispense_ptr] == hoppers[5].hop_name_hash){
    //     hoppers[5].drop_pills(hashedHopperQRs[dispense_ptr+1]);
    //     dispense_ptr+=2;       
    //   }

    //   else if(hashedHopperQRs[dispense_ptr] == hoppers[6].hop_name_hash){
    //     hoppers[6].drop_pills(hashedHopperQRs[dispense_ptr+1]);
    //     dispense_ptr+=2;       
    //   }

    //   else if(hashedHopperQRs[dispense_ptr] == hoppers[7].hop_name_hash){
    //     hoppers[7].drop_pills(hashedHopperQRs[dispense_ptr+1]);
    //     dispense_ptr+=2;       
    //   }

    //   else if(hashedHopperQRs[dispense_ptr] == hoppers[8].hop_name_hash){
    //     hoppers[8].drop_pills(hashedHopperQRs[dispense_ptr+1]);
    //     dispense_ptr+=2;       
    //   }

    //   else if(hashedHopperQRs[dispense_ptr] == hoppers[9].hop_name_hash){
    //     hoppers[9].drop_pills(hashedHopperQRs[dispense_ptr+1]);
    //     dispense_ptr+=2;       
    //   }
    // }
  //   dispensed = true;
  // }  
}

//===============

void package(){
  digitalWrite(17, HIGH);
  delayMicroseconds(100);
}

void pull_package(){
  // Spin motor slowly
  digitalWrite(wrapDirPin, LOW);
  for(int x = 0; x < 9600; x++)
  {
    digitalWrite(wrapStepPin, HIGH);
    delayMicroseconds(1000);
    digitalWrite(wrapStepPin, LOW);
    delayMicroseconds(1000);
  }
  
}

//===============

void finish_package(){
    // Spin motor slowly
  digitalWrite(wrapDirPin, LOW);
  for(int x = 0; x < 10150; x++)
  {
    digitalWrite(wrapStepPin, HIGH);
    delayMicroseconds(1000);
    digitalWrite(wrapStepPin, LOW);
    delayMicroseconds(1000);
  }
}

//===============

void replyToPython() {
    if (serialReceived == true && serialParsed == true) {
        Serial.print('<');
        Serial.println(serialRXArray);    
        for (int i=0; i < parsed_size; i++){
          Serial.println(hashedHopperQRs[i]);
        }
        Serial.print(">");
    }
}

void done(){
  if (dispensed == true){
    Serial.print("<done>");
    serialReceived = false; //Do not adjust, flag used in processing logic
    serialParsed = false; // Sets after the RXArray get's parsed.
    parsedHashed = false; // Sets after the parsedRXArray gets hashed.
    dispensed = false;
    parsed_size = 1;
    hash_size = 0;
    manual_mode = false;
    while (Serial.available() > 0){
      Serial.read();
    }
  }
}
