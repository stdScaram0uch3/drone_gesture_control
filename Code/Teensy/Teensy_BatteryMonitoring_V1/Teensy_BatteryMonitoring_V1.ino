float Voltage, Current, BatteryRemaining, BatteryAtStart;//Define the battery monitoring variables
float CurrentConsumed=0;
float BatteryDefault=1300; //for mAh in the battery

void battery_voltage(void) {
 Voltage=(float)analogRead(15)/62;
 Current=(float)analogRead(21)*0.089; //Measure the voltage and current of the circuit && ((1023 / 3.3 V) x 0.036 V/A)
}

void setup() {
 digitalWrite(5, HIGH);
 battery_voltage();
 if (Voltage > 8.3) { 
  digitalWrite(5, LOW);
  BatteryAtStart=BatteryDefault; }
 else if (Voltage < 7.5) {
   BatteryAtStart=30/100*BatteryDefault ;}
 else { digitalWrite(5, LOW);
   BatteryAtStart=(82*Voltage-580)/100*
   BatteryDefault; }
}

void loop() {
 battery_voltage();
 CurrentConsumed=Current*1000*0.004/3600+CurrentConsumed;
 BatteryRemaining=(BatteryAtStart-CurrentConsumed)/BatteryDefault*100;
 if (BatteryRemaining<=30) digitalWrite(5, HIGH);
 else digitalWrite(5, LOW);
}
