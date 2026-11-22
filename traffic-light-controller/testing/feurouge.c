void setup() {
  pinMode(5,OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
}

void loop() {
 digitalWrite(5, HIGH);
 delay(20000);
 digitalWrite(5, LOW);
 int i=0;
 while(i<6){
   digitalWrite(6, HIGH);
 delay(500);
 digitalWrite(6, LOW);
 i++;
 }
digitalWrite(7, HIGH);
delay(15000);
digitalWrite(7, LOW);

}
