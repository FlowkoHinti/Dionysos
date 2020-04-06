#include <FastLED.h>
#define displayWidth 5
#define displayHight 10
#define baudrate 19200
#define NUM_LEDS ((displayWidth*displayHight)-1)
#define DATA_PIN 11

CRGB leds[(displayWidth*displayHight)];  //Define the array of leds CRGB is an object with red blue and green as attributes

/*
typedef struct{
  short id;
  String color; //color as hex value
  }pixel;
*/

//mit folgenden Pointer bitte die Operationen machen:
//mein Plan: jedes Pixel ist im Array gespeichert und wir updaten die Matrix anhand des Arrays mit einem delay für die Wiederholrate

//pixel *currentDisplay = malloc(sizeof(pixel) * displayWidth * displayHight);  //ned nötig
//short pixelcnt = 0; //ned nötig

void establishConnection();
void exchangeInfo();
bool checkConnection();
void parseSerial();

void setup() {

  FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, (displayWidth*displayHight));  //GRB ordering is assumed
  for (int i = 0; i > NUM_LEDS; ++i) {
     leds[i] = CRGB::Black;
  }
  FastLED.show();

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

  FastLED.show();
  delay(17);


/*-------------------------------------------------------------------

  // Turn the LED on, then pause
  for (int i = 0; i < NUM_LEDS; ++i) {
     leds[i] = CRGB::Red;
     //leds[i] = 0xFF1493;
     FastLED.show();
     delay(10);
  }
  delay(10);
  for (int i = NUM_LEDS; i >= 0; --i) {
     leds[i] = CRGB::Black;
     FastLED.show();
     delay(10);
  }

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
    short x = Serial.parseInt();
    short y = Serial.parseInt();
    long color = Serial.parseInt();
    //hex.concat(Serial.readStringUntil(';'));

    Serial.println(x);
    Serial.println(y);
    Serial.println(color);

    //long color = strtol(hex.c_str(), NULL, 16);

    leds[findID(x,y)] = color;

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

short findID(short x, short y){
  return (x*displayHight + y);
  }
