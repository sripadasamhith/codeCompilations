int photoLED = 13;

void setup() {

  pinMode(A0, INPUT);
  pinMode(photoLED, OUTPUT);
  Serial.begin(9600);
  
}

void loop() {
  
  int sensorVal = analogRead(A0);
  Serial.println(sensorVal);
  digitalWrite(photoLED, HIGH);
  
}
