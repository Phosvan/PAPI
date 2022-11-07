#define charSize 64
char serialRXArray[charSize] = { 0 }; //Initialize a char array of size charSize
bool serialEchoFlag = true; //Set this flag to echo data back to Serial Host. True negatively impacts runtime!!
bool serialReceived = false; //Do not adjust, flag used in processing logic
byte size = 0;

int test1;
int test2;

void setup() {
  Serial.begin(9600);

  char testarr[10] = "kittles";
  char test2arr[10] = "skittles";

  // testarr[9] = '\0';
  // test2arr[9] = '\0';

  test1 = string_hash(testarr);
  test2 = string_hash(test2arr);


}

void loop() {
}

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

