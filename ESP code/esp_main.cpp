#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266HTTPClient.h>
#include <Arduino_JSON.h>

#define SensorPin A0
#define MAX 600
#define MIN 1024
int FloatSensor = 13; //D7
int tank; //tank level
float humidity; // humidity level
float percentage;
int relay = 5; //D1
String Is_empty;
String get_response;
JSONVar my_request;
const char* GET_url = "http://35.243.197.246:5001/api/get_humidity/10fe8791-7ab2-4302-8848-b0a6d280ae48";
const char* PUT_url = "http://35.243.197.246:5001/api/send_data/10fe8791-7ab2-4302-8848-b0a6d280ae48";


// possible wifi network and respective passwords
String ssids [3] = {"Holberton Guest", "Savona", "celebra_ssid"};
String pwds [3] = {"holbertonschoolwifiaccess", "tiasusana", "celebra_pwd"};

// ************* CUIDADO KIKO DEL FUTURO -> EL 3 ESTA HARDCODEADO *********************

void setup() {
  Serial.begin(74880);
  pinMode(FloatSensor, INPUT_PULLUP);
  digitalWrite(relay, HIGH);
  pinMode(relay, OUTPUT);
  // try to connect to a possible wifi network
  for (int i = 0; i < 3; i++) {
    WiFi.begin(ssids[i], pwds[i]);
    Serial.print("Connecting to wifi...");
    while (WiFi.status() != WL_CONNECTED) {
        Serial.print(".");
        delay(1000);
        if (WiFi.status() == 1) {
          break;
        }
    }
    Serial.println("");
    if (WiFi.status() == WL_CONNECTED) {
      break;
    }
  }
  Serial.print("Connected to ");
  Serial.println(WiFi.SSID());
}

// main loop
void loop() {
  get_response = GET_method(GET_url);
  my_request = JSON.parse(get_response);

  JSONVar t = "True";
  if (my_request["Turned_ON"] == t) { // if it is turned on
    Serial.println("Entered ON loop");
    tank = digitalRead(FloatSensor); // read tank state
    humidity = analogRead(SensorPin); // analog read of humidity
    percentage = (float)((humidity - MIN) * 100) / (MAX - MIN); // converts analog read to percentage
    int min_limit = 25;
    int top = int(my_request["Humidity_irrigation"]);
    if  (percentage < min_limit && tank == HIGH) {
        // make calculations of how much seconds to turn on relay, regarding volume, mass etc.
        int bomb_time = (((((top - percentage) * 200) / 75) * 9) / 100) * 1000;
        Serial.println("prendiendo bomba");
        digitalWrite(relay, LOW);
        delay(bomb_time);
        digitalWrite(relay, HIGH);
        tank = digitalRead(FloatSensor); // calculate tank state after irrigation
        for (int milliseconds = 0; milliseconds < 1200000; milliseconds+= 2000) { //120000 millisecods are 20 min
          humidity = analogRead(SensorPin);
          percentage = (float)((humidity - MIN) * 100) / (MAX - MIN);
          if (milliseconds == 0) {
            PUT_method(PUT_url, percentage, tank, "True");
          } else {
            PUT_method(PUT_url, percentage, tank, "False");
          }
          delay(2000); // update info every 2 seconds until 20 minutes are reached
        }
      }
    tank = digitalRead(FloatSensor);
    humidity = analogRead(SensorPin);
    percentage = (float)((humidity - MIN) * 100) / (MAX - MIN);
    Serial.println(humidity);
    PUT_method(PUT_url, percentage, tank, "False");
  }
  delay(2000);
}

// function for the get method of the api
String GET_method(const char* url) {
  WiFiClient client;
  HTTPClient http;

  http.begin(client, url);
  int httpResponseCode = http.GET();
  String payload = "{}"; 
  payload = http.getString();
  http.end();

  return payload;
}

// function for the PUT method of the api
void PUT_method(const char* url, float percentage, int tank, String irrigated) {
  WiFiClient client;
  HTTPClient http;
  
  http.begin(client, url);
  if (tank == 1) {
    Is_empty = "False";
  } else {
    Is_empty = "True";
  }
  http.addHeader("Content-Type", "application/json");
  String request = "{\"irrigated\":\"" + String(irrigated) + "\",\"Is_empty\":\"" + String(Is_empty) + "\",\"Actual_humidity\":\"" + String(percentage) +"\"}";
  Serial.println(request);
  int resp = http.PUT(request);
  http.end();

  return;
}
