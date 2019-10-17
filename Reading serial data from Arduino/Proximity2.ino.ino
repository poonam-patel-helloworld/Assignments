const int TrigPin = 11;
const int EchoPin = 10;

float distance = 0;

void setup() {
  
  Serial.begin(9600);
  Serial.println("0");

  pinMode(TrigPin, OUTPUT);
  pinMode(EchoPin, INPUT);

}

void loop() {

  if(Serial.available() > 0){
    char input = Serial.read();
    distance = getDistance();
    Serial.println(distance);
    delay(50);
  }

}



float getDistance()
{
  float echoTime;                   //variable to store the time it takes for a ping to bounce off an object
  float calculatedDistance;         //variable to store the distance calculated from the echo time
  
  //send out an ultrasonic pulse that's 10ms long
  digitalWrite(TrigPin, HIGH);
  delayMicroseconds(10); 
  digitalWrite(TrigPin, LOW);

  echoTime = pulseIn(EchoPin, HIGH);      //use the pulsein command to see how long it takes for the
                                          //pulse to bounce back to the sensor

  calculatedDistance = echoTime / 148.0;  //calculate the distance of the object that reflected the pulse (half the bounce time multiplied by the speed of sound)
  
  return calculatedDistance;              //send back the distance that was calculated
}
