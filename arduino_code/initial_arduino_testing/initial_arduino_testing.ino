#define green 4
#define red 3
#define button 2
const int mic = A0;
int flagWrite = 0;
int flagRead = 0;

void setup() {
  pinMode(green,OUTPUT);
  pinMode(red,OUTPUT);
  pinMode(button,INPUT);
  Serial.begin(115200);
}

void loop() {
  if (flagWrite == 1){
    Serial.write(analogRead(mic)>>2);
    if (digitalRead(button) == HIGH) {
      while (digitalRead(button) == HIGH){
        delay(0);
      }
      Serial.write(0);
      digitalWrite(green,LOW);
      digitalWrite(red,HIGH);
      flagWrite = 0;
      flagRead = 1;
    }
  }
  else if (flagRead == 1){
    if (Serial.available()){
      if (Serial.read() == 0){
        digitalWrite(red,LOW);
        flagRead = 0;
      }
    }
  }
  else{
    if (digitalRead(button) == HIGH) {
      while (digitalRead(button) == HIGH){
        delay(0);
      }
      Serial.write(0);
      digitalWrite(green,HIGH);
      flagWrite = 1;
    }
  }
}
