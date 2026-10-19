#include <PulsePosition.h>
PulsePositionInput ReceiverInput(RISING);//Use the PulsePosition library

float ReceiverValue[]={0, 0, 0, 0, 0, 0, 0, 0};
int ChannelNumber=0; //Declare the variables to store channel info

float InputThrottle;//Define the throttle variable

void read_receiver(void){ //Define a function to read the receiver data
 ChannelNumber = ReceiverInput.available();
 if (ChannelNumber > 0) {
  for (int i=1; i<=ChannelNumber;i++){
  ReceiverValue[i-1]=ReceiverInput.read(i);
  }
 }
}

void setup() {
 Serial.begin(57600);
 pinMode(13, OUTPUT);
 digitalWrite(13, HIGH);
 ReceiverInput.begin(14);

 analogWriteFrequency(1, 250);//Send PWM signals from your Teensy;;analogWriteFrequency(pin number, PWM frequency)
 analogWriteResolution(12); //higher resolution than 8 bit for PWM output
 delay(250);

 while (ReceiverValue[2] < 1020 ||
  ReceiverValue[2] > 1050) { //by the way RecieverValue[2] corresponds to the throttle input
  read_receiver(); //if the throttle in the beginning is not set to idle, it will refuse to end the setup phase
  delay(4);
 }
 }


void loop() {
 read_receiver();
 InputThrottle=ReceiverValue[2];
 analogWrite(1,1.024*InputThrottle);
}
