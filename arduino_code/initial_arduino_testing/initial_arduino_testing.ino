#define speaker 6
#define green 4
#define red 3
#define button 2
const int mic = A0;
int flagWrite = 0;
int flagRead = 0;
int audio = -1;

void setup() {
  pinMode(speaker,OUTPUT);
  pinMode(green,OUTPUT);
  pinMode(red,OUTPUT);
  pinMode(button,INPUT);
  Serial.begin(115200);
  TCCR0B = 0b00000001;
  TCCR0A = 0b00000011;
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
      //Serial.print(Serial.read());
      //audio = Serial.read();
      analogWrite(speaker, Serial.read()<<2);//audio);
      //if (audio == 0){
      //  digitalWrite(red,LOW);
      //  flagRead = 0;
      //}
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
