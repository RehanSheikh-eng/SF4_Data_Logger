#define LED 2
#define button 3
const int microphonePin = A0;
int flag = 0;

void setup() {
//  pinMode(LED,OUTPUT);
  Serial.begin(115200);
}

void loop() {
  //if (digitalRead(button) == LOW) {

    //digitalWrite(LED,HIGH);
    //flag = 0;

    Serial.write(analogRead(microphonePin)>>2);
  //}
  //else {
    //digitalWrite(LED,LOW);
    //if (flag == 0){
      //Serial.println();
      //flag = 1;
    //}
  //}
}
