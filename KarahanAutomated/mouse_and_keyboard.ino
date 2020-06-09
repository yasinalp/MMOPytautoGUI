#include <Keyboard.h>
#include <Mouse.h>

String receivedStr;
char firstChar;
String firstCharInt;
char secondChar;
int firstCommaIndex;

void setup() {
  // put your setup code here, to run once:
  pinMode(10,INPUT);
  pinMode(12,OUTPUT);
  digitalWrite(12,HIGH);
  Serial.begin(9600);
  Keyboard.begin();
  Mouse.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(10)==LOW)
  {
    Keyboard.releaseAll();
    Mouse.release();
  }
  if(Serial.available()>0 && digitalRead(10)==HIGH)
  {
    receivedStr = Serial.readStringUntil(']');

    if(receivedStr.indexOf('[')!=-1)
    {
      receivedStr = receivedStr.substring(receivedStr.indexOf('[')+1);
      firstCommaIndex = receivedStr.indexOf(',');
      firstChar = receivedStr[firstCommaIndex-1];
      firstCharInt = receivedStr.substring(0,firstCommaIndex);//.toInt();
      //Serial.print("firstCharInt:");
      //Serial.print(firstCharInt);
      if(firstCharInt.length()>1)
      {
        //Serial.print("firstCharInt bigger than 9");
        firstChar = char(firstCharInt.toInt());
      }
      secondChar = receivedStr[firstCommaIndex+1];
    }

    if(secondChar=='0')
    {
      Keyboard.release(firstChar);
    }
    else if(secondChar=='1')
    {
      Keyboard.press(firstChar);
    }
    else if(secondChar=='2')
    {
      Keyboard.write(firstChar);
    }
    else if(secondChar=='3')
    {
      if(firstChar=='0')
      {
        Mouse.press();
      }
      Serial.write("Mouse pressed");
    }
    else if(secondChar=='4')
    {
      if(firstChar=='0')
      {
        Mouse.release();
      }
      Serial.write("Mouse released");
    }
    else if(secondChar=='5')
    {
      if(firstChar=='0')
      {
        Mouse.click();
      }
      Serial.write("Mouse clicked");
    }
  }
}
