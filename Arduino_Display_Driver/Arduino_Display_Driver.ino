#include <Adafruit_NeoPixel.h>

#define displayWidth 10
#define displayHight 20
#define baudrate 19200

void establishConnection();
void exchangeInfo();
bool checkConnection();

typedef struct{
  short id;
  short red;
  short green;
  short blue;
  }pixel;

//mit folgenden Pointer bitte die Operationen machen:
//mein Plan: jedes Pixel ist im Array gespeichert und wir updaten die Matrix anhand des Arrays mit einem delay für die Wiederholrate
pixel *currentDisplay = malloc(sizeof(pixel) * displayWidth * displayHight);

void setup() {
  // put your setup code here, to run once:
 
  Serial.begin(baudrate);
  establishConnection();
  exchangeInfo();
}


void loop() {
  // put your main code here, to run repeatedly:
  //Wie die Main()
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

bool checkConnection(){
  //Für Überprüfung 
  
  
  return true;
}
