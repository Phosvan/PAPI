#include <Stepper.h>
#include <Servo.h>
#define P 53
#define M (int)pow(9, 9) + 9
#define charSize 64
#define ir_digital 16
#define ir_drop -100
#define turnSpeed 1300                                             
#define turnStop 1500


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
    
    bool does_exist;

    void set_Hopper(Servo srvo, int pin, uint8_t ir_pin){
      this->srvo = srvo;      
      this->srvo.attach(pin);
      this->srvo.writeMicroseconds(turnStop);

      this->ir.set_pin(ir_pin);
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
      bool count = true;
      while (amount > 0){
        if (this->ir.c > ir_drop){
          count = true;
        }

        this->srvo.writeMicroseconds(turnSpeed);
        digitalWrite(ir_digital,HIGH);    // Turning ON LED
        delayMicroseconds(500);  //wait
        this->ir.calc_a();        //take reading from photodiode(pin A3) :noise+signal
        digitalWrite(ir_digital,LOW);     //turn Off LED
        delayMicroseconds(500);  //wait
        this->ir.calc_b();      // again take reading from photodiode :noise
        this->ir.calc_c();   

        Serial.println(this->ir.c);

        if (this->ir.c < ir_drop && count == true){
          count = false;
          amount--;        
        }
      }
      this->srvo.writeMicroseconds(turnStop);
    }
};

Hopper hoppers[] = {
  Hopper()
};

// Yellow step, Green direct
Stepper step = Stepper(100, 3, 22);

char serialRXArray[charSize] = { 0 }; //Initialize a char array of size charSize
char serial1RXArray[charSize] = { 0 }; //Initialize a char array of size charSize

char parsedRXArray[12][64];
int parsed_size = 1; // Due to the way parsing is done.

int hashedHopperQRs[10] = { 0 };
int hash_size = 0;

bool serialEchoFlag = false; //Set this flag to echo data back to Serial Host. True negatively impacts runtime!!
bool serialReceived = false; //Do not adjust, flag used in processing logic
bool serialParsed = false; // Sets after the RXArray get's parsed.
bool parsedHashed = false; // Sets after the parsedRXArray gets hashed.
bool pills_dispensed = false;

bool calibrate = false;

bool debug = true; // Prints shit to the pi for viewing
//===============

void setup() {
  pinMode(16, OUTPUT);
  step.setSpeed(1000);

  Serial.begin(9600);
  Serial.println("<Arduino is ready>");

  hoppers[0].set_Hopper(Servo(), 6, A4);
  char apple_str[]  = "apple";
  hoppers[0].set_qr(apple_str);
}

//===============

void loop() {
  
  // if (calibrate){
  //   calibration();
  // }
  // else{
  //   Serial.print("<run>");
  // }

  serialRead();
  serialParse();
  hash_hoppers();
  dispense_pills();

  if (debug){
    replyToPython();
  }
  // done();
}

//===============

void calibration(){
  int count = 0;
  char confirmed[] = "confirmed";
  Serial.print("<calibrate>");
  
  while (true){
    serialRead();
    if (Hopper::string_hash(serialRXArray) == Hopper::string_hash(confirmed)){
      break;
    }
    serialReceived = false;
  }
  Serial.print("continue");
  while (calibrate) {
    step.step(1500);

    serialRead();
    if (serialReceived){
      hoppers[count].set_qr(serialRXArray);
      serialReceived = false;
      Serial.print("continue");      
      count++;
    }

    if (count == 1){
      step.step(0);
      calibrate = false;
      serialReceived = false;
      break;
    }

  }
    
  
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
    static byte upper_ptr = 0; // Indicative of position in first dimension
    static byte lower_ptr = 0; // Indicative of position in second dimension
    static byte i;
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

void hash_hoppers(){
  static byte hash_ptr = 0;
  static byte parsed_ptr = 3;
  if (serialParsed) {
    for (int i = parsed_ptr; parsed_ptr < parsed_size-1; i++) {
      hashedHopperQRs[hash_ptr++] = Hopper::string_hash(parsedRXArray[parsed_ptr]);
      hashedHopperQRs[hash_ptr++] = atoi(parsedRXArray[parsed_ptr+1]);
      hash_size+=2;
      parsed_ptr+=2;    
    }
    parsedHashed = true;
  }
}

//===============

void dispense_pills(){
  static byte ptr = 0;
  if (parsedHashed){
    while (ptr < hash_size-1){
      if (hashedHopperQRs[ptr] == hoppers[0].qr_hash){
        hoppers[0].drop_pills(hashedHopperQRs[ptr+1]);
        ptr+=2;       
      }
    }
  }
}

//===============

void replyToPython() {
    if (serialReceived == true) {
        Serial.print('<');
        Serial.println(serialRXArray);    
        for (int i=0; i < parsed_size; i++){
          Serial.println(hashedHopperQRs[i]);
        }
        Serial.print(">");
    }
}

void done(){
  if (serialReceived == true){
    Serial.print("<done>");
    serialEchoFlag = false; //Set this flag to echo data back to Serial Host. True negatively impacts runtime!!
    serialReceived = false; //Do not adjust, flag used in processing logic
    serialParsed = false; // Sets after the RXArray get's parsed.
    parsedHashed = false; // Sets after the parsedRXArray gets hashed.
    pills_dispensed = false;
  }
}
