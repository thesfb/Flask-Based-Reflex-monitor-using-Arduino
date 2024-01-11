int ledPins[] = {9, 10, 11, 12}; 
int sensorPins[] = {5,4,3,2}; 
int ranLED;
int ranDelay = 0;
float realTime;

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 4; i++) {
    pinMode(ledPins[i], OUTPUT);
    pinMode(sensorPins[i], INPUT);
  }
  randomSeed(analogRead(0));
}

void loop() {

  
  Serial.println("Push the button to start game");

  while (digitalRead(sensorPins[0]) == 0 && digitalRead(sensorPins[1]) == 0 &&
         digitalRead(sensorPins[2]) == 0 && digitalRead(sensorPins[3]) == 0) {
  }

  for (int i = 0; i < 4; i++) {
   
    ranLED = random(0,4);
    blinkLED(ledPins[ranLED], sensorPins[ranLED]);
  }
}

void blinkLED(int ledPin, int sensorPin) {
  Serial.println("Get Ready!");
  delay(1000);
  Serial.println("Get Set!");
  delay(1000);
  ranDelay = random(5000);
  delay(ranDelay);
  Serial.println("Go!");

  realTime = millis();
  digitalWrite(ledPin, HIGH);

  while (digitalRead(sensorPin) == 0) {
  }

  digitalWrite(ledPin, LOW);
  Serial.println("Your time was");
  realTime = millis() - realTime;
  Serial.println(realTime / 1000, 2);
  Serial.println("seconds");
  delay(2000);
}
