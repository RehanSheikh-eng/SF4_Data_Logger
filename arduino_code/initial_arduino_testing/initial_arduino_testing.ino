#define LED 2
#define button 3
const int microphonePin = A0;
int flag = 0;

void setup() {
  pinMode(LED,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (digitalRead(button) == LOW) {

    digitalWrite(LED,HIGH);
    flag = 0;
    
    int min = 1024;
    int max = 0;

    for (int i = 0; i < 90; ++i) {
      int val = analogRead(microphonePin);
      max = max(max, val);
      min = min(min, val);
    }

    int delta = max - min;

    Serial.print(delta);
    Serial.print(" ");
  }
  else {
    digitalWrite(LED,LOW);
    if (flag == 0){
      Serial.println();
      flag = 1;
    }
  }
}
