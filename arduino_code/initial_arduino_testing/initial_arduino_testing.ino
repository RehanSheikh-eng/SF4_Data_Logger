// #define LED 2
// #define BUTTON 3
// #define MIC_PIN A0

// const int BAUD_RATE = 9600; 
// const int BUFFER_SIZE = 1024; 

// uint8_t buffer[BUFFER_SIZE]; 
// int bufferIndex = 0; 

// enum State {
//   WAITING,
//   RECORDING,
// };

// State currentState = WAITING;

// void setup() {
//   pinMode(LED, OUTPUT);
//   pinMode(BUTTON, INPUT_PULLUP);
//   Serial.begin(BAUD_RATE);
// }

// void loop() {
//   switch (currentState) {
//     case WAITING:
//       if (digitalRead(BUTTON) == LOW) {
//         currentState = RECORDING;
//         digitalWrite(LED, HIGH);
//         bufferIndex = 0;
//       }
//       break;

//     case RECORDING:
//       int mn = 1024;
//       int mx = 0;
      
//       if (digitalRead(BUTTON) == HIGH) {
//         currentState = WAITING;
//         digitalWrite(LED, LOW);
//       } else {
//         for (int i = 0; i < 10000; ++i) {
//           int micValue = analogRead(MIC_PIN); 

//           mn = min(mn, micValue);
//           mx = max(mx, micValue);

//           buffer[bufferIndex++] = (mx - mn) >> 2;

//           if (bufferIndex >= BUFFER_SIZE) {
//             if (Serial) {
//               Serial.write(buffer, BUFFER_SIZE);
//             } else {
//               // Handle the error here.
//             }
//             bufferIndex = 0;
//           }
//         }
//       }
//       break;
//   }
// }
const int microphonePin = A0;
const int buttonPin = 2; // adjust this to the correct pin
bool isRecording = false;

void setup() {
  pinMode(buttonPin, INPUT_PULLUP); // button is expected to connect to GND when pressed
  Serial.begin(9600);
}

void loop() {
  if (digitalRead(buttonPin) == LOW) { // button is pressed
    if (!isRecording) { // start recording
      isRecording = true;
      Serial.println("<start>"); // start marker
    }
    int val = analogRead(microphonePin);
    Serial.println(val);
  } else {
    if (isRecording) { // stop recording
      isRecording = false;
      Serial.println("<stop>"); // stop marker
    }
  }
}
