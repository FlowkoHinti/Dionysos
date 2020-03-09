#include <Adafruit_NeoPixel.h>

#define displayWidth 10
#define displayHight 20
#define baudrate 19200

typedef struct{
  short id;
  short red;
  short green;
  short blue;
  }pixel;

//mit folgenden Pointer bitte die Operationen machen:
//mein Plan: jedes Pixel ist im Array gespeichert und wir updaten die Matrix anhand des Arrays mit einem delay für die Wiederholrate
pixel *currentDisplay = malloc(sizeof(pixel) * displayWidth * displayHight);
short pixelcnt = 0;

void establishConnection();
void exchangeInfo();
bool checkConnection();
void parseSerial();

void setup() {
  Serial.begin(baudrate);
  establishConnection();
  exchangeInfo();
}


void loop() {
  if (Serial.available() > 0){
    //checkConnection vllt? (Notiz an mich selbst)
    //interrupt wenn daten vohanden sind
      parseSerial();
    }


    /*
     * HIER DEIN CODE
     * 
     * 
     */


    
  
}

void toDisplay(){
  //HIER DEIN CODE
  //kannst ja noch weitere Funktionen hinzufügen fallst du brauchst
}



void establishConnection(){
  //Baut die Verbindung auf
  if (Serial){
    while(Serial.available() == 0){
        Serial.println("SYN");
        delay(100);
    }
    Serial.println("ACK");
  }
}

void exchangeInfo(){
  //Größe des Displays
  Serial.println(String(displayWidth));
  Serial.println(String(displayHight));
}

void parseSerial(){
  if(Serial.parseInt() == 0){
    short x = Serial.parseInt();
    short y = Serial.parseInt();
    short r = Serial.parseInt();
    short g = Serial.parseInt();
    short b = Serial.parseInt();
  }
  //Bitte erweitern
  
  

}

void findID(short x, short y){
  //--> FINDE die ID anhand von x und y Positionen
  
  }


bool checkConnection(){
  //Für Überprüfung 
  
  return true;
}
