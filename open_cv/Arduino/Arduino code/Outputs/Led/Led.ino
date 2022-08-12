#include<cvzone.h>
SerialData serialData(1,1);
int valsRec[1];

void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
  serialData.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  serialData.Get(valsRec);  
  digitalWrite(13,valsRec[0]);
  
}
