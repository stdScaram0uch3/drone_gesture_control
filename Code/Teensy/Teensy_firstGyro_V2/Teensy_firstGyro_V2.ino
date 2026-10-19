#include <Wire.h>

float RateRoll, RatePitch, RateYaw;

float RateCalibrationRoll, RateCalibrationPitch, RateCalibrationYaw;
int RateCalibrationNumber; //Declare the calibration variables

void gyro_signals(void) {
 Wire.beginTransmission(0x68); //Start I2C communication with the gyro
 
 Wire.write(0x1A);
 Wire.write(0x05);
 Wire.endTransmission(); //Switch on the lowpass filter
 
 Wire.beginTransmission(0x68);
 Wire.write(0x1B);
 Wire.write(0x8);
 Wire.endTransmission(); //Set the sensitivity scale factor

 Wire.beginTransmission(0x68);
 Wire.write(0x43);
 Wire.endTransmission(); //Access registers storing gyro measurements

 Wire.requestFrom(0x68,6); //Request 6 bytes from the MPU-6050 such that you can pull the information of the 6 registers 43 to 48 from the sensor.

 int16_t GyroX=Wire.read()<<8 | Wire.read(); //(merging information of 2 8bit Registers) 
 int16_t GyroY=Wire.read()<<8 | Wire.read();
 int16_t GyroZ=Wire.read()<<8 | Wire.read();//Read the gyro measurements around theX, Y and Z axis

 RateRoll=(float)GyroX/65.5;
 RatePitch=(float)GyroY/65.5;
 RateYaw=(float)GyroZ/65.5; //Convert the measurement units to °/s
}
void setup() {
 Serial.begin(57600);
 pinMode(13, OUTPUT);
 digitalWrite(13, HIGH);

 Wire.setClock(400000); //speed: 400 kHz
 Wire.begin(); //Set the clock speed of I2C
 delay(250); //giving her time to start

 Wire.beginTransmission(0x68);
 Wire.write(0x6B);
 Wire.write(0x00); //Start the gyro in power mode

 Wire.endTransmission();

 for (RateCalibrationNumber=0; RateCalibrationNumber<2000; RateCalibrationNumber ++) {
   gyro_signals(); // Perform the calibration measurements
   RateCalibrationRoll+=RateRoll;
   RateCalibrationPitch+=RatePitch;
   RateCalibrationYaw+=RateYaw;
   delay(1); //2000 measurements à 1ms
 }

 RateCalibrationRoll/=2000;
 RateCalibrationPitch/=2000;
 RateCalibrationYaw/=2000; //calculating the avege value

 digitalWrite(13, LOW);
}

void loop() {
 gyro_signals();

 RateRoll-=RateCalibrationRoll; //correcting the values
 RatePitch-=RateCalibrationPitch;
 RateYaw-=RateCalibrationYaw;
 
 Serial.print("Roll rate [°/s]= ");
 Serial.print(RateRoll);
 Serial.print(" Pitch Rate [°/s]= ");
 Serial.print(RatePitch); //Call the predefined function to read the gyro measurements
 Serial.print(" Yaw Rate [°/s]= ");
 Serial.println(RateYaw);
 delay(50);
}
