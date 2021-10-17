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
String get_response;
JSONVar my_request;
String GET_url = "http://35.243.197.246:5001/api/get_humidity";
String PUT_url = "http://35.243.197.246:5001/api/send_data";


// possible wifi network and respective passwords
String ssids [3] = {"hbtn_ssid", "Savona", "celebra_ssid"};
String pwds [3] = {"hbtn_pwd", "tiasusana", "celebra_pwd"};

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

  if (my_request["Turned_ON"] == "True") { // if it is turned on
    tank = digitalRead(FloatSensor); // read tank state
    humidity = analogRead(SensorPin); // analog read of humidity
    percentage = (float)((humidity - MIN) * 100) / (MAX - MIN); // converts analog read to percentage
    int min_limit = 20;
    int water = my_request["Humidity_irrigation"];
    if  (percentage < min_limit && tank == HIGH) {
        // make calculations of how much seconds to turn on relay, regarding volume, mass etc. (in line below)
        // this one
        digitalWrite(relay, LOW);
        delay(/* x seconds calculated */);
        digitalWrite(relay, HIGH);
        tank = digitalRead(FloatSensor); // calculate tank state after irrigation
        for (int minutes = 0; minutes < 30; minutes += 2) {
          humidity = analogRead(SensorPin);
          percentage = (float)((humidity - MIN) * 100) / (MAX - MIN);
          if (minutes == 0) {
            PUT_method(PUT_url, percentage, tank, "True");
          } else {
            PUT_method(PUT_url, percentage, tank, "False");
          }
          delay(120000);
        }
      }
    tank = digitalRead(FloatSensor);
    humidity = analogRead(SensorPin);
    percentage = (float)((humidity - MIN) * 100) / (MAX - MIN);
    PUT_method(PUT_url, percentage, tank, "False");
  }
}

// function for the get method of the api
String GET_method(String url) {
  WiFiClient client;
  HTTPClient http;
  
  http.begin(client, url);
  String payload = "{}"; 
  payload = http.getString();
  http.end();

  return payload;
}

// function for the PUT method of the api
String PUT_method(String url, float percentage, int tank, String irrigated) {
  WiFiClient client;
  HTTPClient http;
  
  http.begin(client, url);
  http.addHeader("Content-Type", "application/json");
  if (tank == 1) {
    String Is_empty = "False";
  } else {
    String Is_empty = "True";
  }
  String request = "{\"irrigated\":" + irrigated + ",\"Is_empty\":" + Is_empty + ",\"Actual_humidity\":" + percentage +"}";
  http.PUT(request);
  http.end();

  return payload;
}