int led = 13;

void setup() {
  pinMode(led, OUTPUT);
  
  //Serial.begin(115200);
}

void loop() {
  digitalWrite(led, HIGH);
  delay(400);
  digitalWrite(led, LOW);
  delay(100);q
}
