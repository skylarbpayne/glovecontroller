//Author: Skylar Payne
// This file defines the running program for the Hacktech.io Glove
//project by Skylar Payne, Yvonne Fung, Max Camacho, and Allen Sallinger.

//These are all the pin numbers for the analog sensors
int thumbSensor = 0;
int middleSensor = 1;
int indexSensor = 2;
int accelX = 3;
int accelY = 4;
int accelZ = 5;

//Variables to store the readings from each analog sensor
int thumbReading = 0;
int middleReading = 0;
int indexReading = 0;
int accelXReading = 0;
int accelYReading = 0;
int accelZReading = 0;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
    if(Serial.available() > 0)
    {
      //Because these values will be sent wireless, we scale the numbers down to a single byte.
      thumbReading = map(analogRead(thumbSensor), 0, 1023, 0, 255);
      middleReading = map(analogRead(middleSensor), 0, 1023, 0, 255);
      indexReading = map(analogRead(indexSensor), 0, 1023, 0, 255);
      accelXReading = map(analogRead(accelX), 0, 1023, 0, 255);
      accelYReading = map(analogRead(accelY), 0, 1023, 0, 255);
      accelZReading = map(analogRead(accelZ), 0, 1023, 0, 255);
      
      //Send each value to the XBee
      Serial.write(thumbReading);
      Serial.write(middleReading);
      Serial.write(indexReading);
      Serial.write(accelXReading);
      Serial.write(accelYReading);
      Serial.write(accelZReading);
    }
    
    delay(50);
}


