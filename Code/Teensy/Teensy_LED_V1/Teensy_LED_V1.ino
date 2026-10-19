//pin 13 is inbuilt led

void setup() {
  pinMode(13, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  digitalWrite(13, HIGH);
  digitalWrite(5, HIGH);
  delay(4000);
  digitalWrite(5, LOW);
  digitalWrite(6, HIGH);
  
  //Serial.begin(115200);
}

void loop() {
}
