// Download libraries for LCD
#include <Wire.h>
#include "rgb_lcd.h"

// Match input and output pins to variables
#define green 5
#define yellow 4
#define red 3
#define button 2
const int mic = A0;
rgb_lcd lcd;

// Define working values for LCD text
char LineOne[16];
char LineTwo[16];
char CharIn = "";
int LineLen = 0;
int LineIndex = 0;
int NewLine = 0;
int DoubleDigits = 0;

// Define flags (states) for overall operation
int flagWrite = 0;
int flagWait = 0;
int flagRead = 0;

void setup() {
  
  // Define digital pins as inputs or outputs
  pinMode(green,OUTPUT);
  pinMode(yellow,OUTPUT);
  pinMode(red,OUTPUT);
  pinMode(button,INPUT);

  Serial.begin(115200); // Setup serial connection
  lcd.begin(16, 2); // Define size of LCD
  
  // Fill output text char arrays with spaces
  for (int i = 0; i < 16; i++){
    LineOne[i] = 0x14;
    LineTwo[i] = 0x14;
  }

  // Display starting message
  lcd.print("Press the button");
  lcd.setCursor(0, 1);
  lcd.print("give me an idea!");
  lcd.setCursor(0, 0);
}

void loop() {

  if (flagWrite == 1){ // Recording

    Serial.write(analogRead(mic)>>2); // Send recorded data out serial connection
    
    // Stop recording if button pressed
    if (digitalRead(button) == HIGH) {
      
      // Wait until button released before changing state
      while (digitalRead(button) == HIGH){
        delay(0);
      }

      // Send 0 byte to indicate recording is finished
      Serial.write(0);
      
      // Change LED switched ON (yellow) to indicate to user recording is finished
      digitalWrite(red,LOW);
      digitalWrite(yellow,HIGH);

      // Change state
      flagWrite = 0;
      flagWait = 1;
    }
  }
  else if (flagWait == 1){ // Waiting
    if (Serial.available() > 0){ // Check if Data received
      
      // Wait until beginning of text signal
      if (Serial.read() == 35){
        // Change LED switched ON (green) to indicate to user recording is finished
        digitalWrite(yellow,LOW);
        digitalWrite(green,HIGH);

        // Clear display ready to start telling story
        lcd.clear();

        // Change state
        flagWait = 0;
        flagRead = 1;
      }
    }
  }
  else if (flagRead == 1){ // Telling story
    if (Serial.available() > 0){ // Check if Data received

      // Store Character
      CharIn = Serial.read();
      if (CharIn == 35){ // End of text signal
        digitalWrite(green,LOW); // Turn red LED OFF to indicate to user end of story
        flagRead = 0; // Change state
      }
      else if (CharIn == 126){ // Word length has double digits signal
        DoubleDigits = 1;
      }
      else{
        // If Character is a digit (equal to length of word) it marks start of word
        if (isdigit(CharIn)){
          if (DoubleDigits == 1){
            LineLen += CharIn - 38; // Subtract 38 (0 in bytes - 10) to get double digit word length
          }
          else{
            LineLen += CharIn - 48; // Subtract 48 (0 in bytes) to get word length
          }
          
          // If word not at the beginning of the line need to add a space to separate from previous word
          if (LineIndex > 0){
            LineLen ++;
          }

          //If total line length greater than 16, out of display, need to move to new line
          if (LineLen > 16){
            
            // Add word length to new line
            if (DoubleDigits == 1){
              LineLen = CharIn - 38;
            }
            else{
              LineLen = CharIn - 48;
            }
            LineIndex = 0; //Reset index to start text at beginning of line
            
            // If end of first line, need to start at beginning of second line
            if (NewLine == 0){
              NewLine = 1;
              lcd.setCursor(0, 1);
            }

            // If end of second line, need to move second line to first line and start again at beginning of second line
            else{
              lcd.clear();

              // Move second line to first line
              lcd.setCursor(0, 0);
              for (int i = 0; i < 16; i++){
                lcd.print(LineTwo[i]);
                LineOne[i] = LineTwo[i];
                LineTwo[i] = 0x14;
              }

              // Start at beginning of second line
              lcd.setCursor(0, 1);
            }
          }

          // If not at the beginning of the line, need to add a space to separate from previous word
          else if (LineIndex > 0){
            CharIn = 0x14; // Space encoded by byte = 20
            if (NewLine == 0){
              LineOne[LineIndex] = CharIn;
            }
            else {
              LineTwo[LineIndex] = CharIn;
            }
            lcd.print(CharIn);
            LineIndex ++;
          }
          DoubleDigits = 0; // Reset word length to single digit after second digit read
        }
      
        // The length of the word and fitting it within the line is already accounted for using the above
        // Just need to print word one character at a time
        else{
          if (NewLine == 0){
            LineOne[LineIndex] = CharIn;
          }
          else {
            LineTwo[LineIndex] = CharIn;
          }
          lcd.print(CharIn);
          LineIndex ++;
        }
      }
    }
  }
  else{ // Neither recording or telling story
    
    // If button pressed change state to record
    if (digitalRead(button) == HIGH) {

      // Wait until button released before changing state
      while (digitalRead(button) == HIGH){
        delay(0);
      }

      Serial.write(0); // Send 0 byte to indicate start of recording
      digitalWrite(red,HIGH); // Turn green LED ON to indicate to user start of recording
      flagWrite = 1; // Change state
    }
  }
}

