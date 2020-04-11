#include <FastLED.h>
#define displayWidth 5
#define displayHight 10
#define baudrate 9600
#define NUM_LEDS ((displayWidth*displayHight)-1)
#define DATA_PIN 11

CRGB leds[(displayWidth*displayHight)];  //Define the array of leds CRGB is an object with red blue and green as attributes

void establishConnection();
void exchangeInfo();
bool checkConnection();
void parseSerial();
bool x = false;


void setup() {

  FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, (displayWidth*displayHight));  //GRB ordering is assumed
  //Turn all LEDS off
  for (int i = 0; i > NUM_LEDS; ++i) {
     leds[i] = CRGB::Black;
  }

  
  FastLED.setBrightness(10);
  FastLED.show();

  Serial.begin(baudrate);
  //establishConnection();
  //exchangeInfo();
}


void loop() {  
  while (Serial.available() >= 7){
      parseSerial();
      //FastLED.show();
      if (x == false){
        x = true;
      }
    }

    if (x == true){
      FastLED.show();
      x = false;
    }
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


void parseSerial(){
  
  String received = "";
  if(Serial.read() == '['){
    received = Serial.readStringUntil(']');
    Serial.println(received);

    short x_len = received.indexOf(',');
    short y_len = received.indexOf(',', x_len+1);
    short c_len = received.indexOf(']');
    
    String str_x = received.substring(0,x_len);
    String str_y = received.substring(x_len+1,y_len);
    String str_c = received.substring(y_len+1,c_len);
    //Serial.println(str_x);
    //Serial.println(str_y);
    //Serial.println(str_c);

    leds[findID(str_x.toInt(), str_y.toInt())] = str_c.toInt();
  }
    /*
    short x = Serial.parseInt(SKIP_ALL);
    short y = Serial.parseInt(SKIP_ALL);
    long color = Serial.parseInt(SKIP_ALL);
    //Serial.println(x);
    //Serial.println(y);
    //Serial.println(color);
    leds[findID(x,y)] = color;
    */
}


short findID(short x, short y){
  if (x%2 != 0){
    return ((((x+1)*displayHight) -y)-1);
  } else {
    return ((x*displayHight) + y);
  }
}
