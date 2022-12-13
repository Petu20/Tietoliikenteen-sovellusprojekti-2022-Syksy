#include "messaging.h"
#include "accelerator.h"

void setup() 
{
  Serial.begin(19200);
}

void loop()
{
  Accelerator Aobject;
  Messaging Mobject;
  Serial.println("Give number how many measurements");
  int NumberOfMeasurements = 0;
  while(NumberOfMeasurements==0)
  {
    if(Serial.available()>0)
    {

      NumberOfMeasurements = Serial.parseInt();
      //NumberOfMeasurements = 0;
      Aobject. makeMeasurement();
      Measurement a = Aobject. getMeasurement();
      Serial.print(a.x);
      Serial.print(a.y);
      Serial.println(a.z);
    }
  }

//TRANSMITTER(PIENI VEMPELE PINNIIN 12)
//RECEIVER (ISO VEMPELE PINNIIN 11)
  for(int M = 0;M<NumberOfMeasurements;M++)
  {
     Aobject.makeMeasurement();
     Measurement m = Aobject.getMeasurement();
     uint8_t id = M;
     uint8_t flags = 0xff;
     Mobject.createMessage(m);
     if(Mobject.sendMessage(id,flags))
     {
       Serial.println("Successfull transmission");
     }
     else
     {
       Serial.println("Transmission fails");
     }
     if(Mobject.receiveACK())
     {
       Serial.println("Receiver got message, going to next measurement");
     }
     else
     {
       Serial.println("Reciver did not get the message. Need to resend it");
       M--;  // Let's just revind for loop 
     }
  } // end of for
}   // end of loop
