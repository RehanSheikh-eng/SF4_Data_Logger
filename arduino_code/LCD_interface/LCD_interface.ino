#include <Wire.h>
#include "rgb_lcd.h"
rgb_lcd lcd;
char LineOne[16];
char LineTwo[16];
char CharIn = "";
int LineLen = 0;
int LineIndex = 0;
int LineNum = 0;

void setup() {
  Serial.begin(115200);
  lcd.begin(16, 2);
  for (int i = 0; i < 16; i++){
    LineOne[i] = 0x14;
    LineTwo[i] = 0x14;
  }
}

void loop() {
  if (Serial.available() > 0){
    CharIn = Serial.read();
    if (isdigit(CharIn)){
      LineLen += CharIn - 48;
      if (LineIndex > 0){
        LineLen ++;
      }
      if (LineLen > 16){
        LineLen = CharIn - 48;
        LineIndex = 0;
        if (LineNum == 0){
          LineNum ++;
          lcd.setCursor(0, 1);
        }
        else{
          lcd.clear();
          lcd.setCursor(0, 0);
          for (int i = 0; i < 16; i++){
            lcd.print(LineTwo[i]);
            LineOne[i] = LineTwo[i];
            LineTwo[i] = 0x14;
          }
          lcd.setCursor(0, 1);
        }
      }
      else if (LineIndex > 0){
        CharIn = 0x14;
        if (LineNum == 0){
          LineOne[LineIndex] = CharIn;
        }
        else {
          LineTwo[LineIndex] = CharIn;
        }
        lcd.print(CharIn);
        LineIndex ++;
      }
    }
    else{
      if (LineNum == 0){
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
