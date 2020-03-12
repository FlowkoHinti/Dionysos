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
     * soll vllt den Display immer updaten
     * und danach vllt ein Delay ?
     */


    
  //free(currentDisplay);
}


void establishConnection(){
  //Baut die Verbindung auf
  if (Serial){
    while(Serial.available() == 0){
        Serial.println("SYN");
        delay(100);
    }
    Serial.println("SOGENUGACK");
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

void parseSerial(){
    bool on_off = Serial.parseInt();
    short x = Serial.parseInt();
    short y = Serial.parseInt();
    String hex = "0";
    hex.concat(Serial.readStringUntil(';'));
    

    Serial.println(on_off);
    Serial.println(x);
    Serial.println(y);
    Serial.println(hex);


    /*--> bekommt von Display Klasse : 
     * on_off (true ein / false aus)
     * x Position (sollte zwischen 0 und max width sein)
     * y Postion (sollte zwischen 0 und max hight sein)
     * hex String = 0x... wird auch schon richtig zusammengefügt
     * 
     * So hier also bitte noch den aufruf für die findID Funktion 
     * und danach natürlich die positionen mit extra Funktion/en in das Display Array einfügen
     * bzw löschen
     */




  
  

}
/*
 * Hier deine Add Pixel Delete Pixel Funktion/en
 * 
 * 
 */

void findID(short x, short y){
  //--> FINDE die ID anhand von x und y Positionen
  //Bitte machen
  
  }
