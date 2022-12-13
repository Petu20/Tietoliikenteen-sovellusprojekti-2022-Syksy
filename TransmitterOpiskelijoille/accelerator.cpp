#include "accelerator.h"
#include <arduino.h>

Accelerator::Accelerator()
{
   Serial.println("Accelerator created!");
}


Accelerator::~Accelerator()
{
   Serial.println("Accelerator deleted!");
}

 const int VccPin2 = A0;  // Käyttöjännite
 const int xPin   = A1;   // x-kanavan mittaus
 const int yPin   = A2;   // y-kanava
 const int zPin   = A3;   // z-kanava
 const int GNDPin2 = A4;  // laitteen maa-napa

 int x = 0;
 int y = 0;
 int z = 0;

void Accelerator::makeMeasurement()
{
 pinMode(VccPin2, OUTPUT); 
 pinMode(GNDPin2, OUTPUT);

 digitalWrite(VccPin2, HIGH);
 digitalWrite(GNDPin2, LOW);

  
  m.x + analogRead(A1); //my.x = measurement m.int x eli int x,y,z h filessä
  m.y + analogRead(A2);
  m.z + analogRead(A3);
}
Measurement Accelerator::getMeasurement()
{
 return m;
}
