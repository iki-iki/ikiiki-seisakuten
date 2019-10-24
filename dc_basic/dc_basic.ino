int out_pin = 13;

void setup() {
    pinMode(out_pin, OUTPUT);
    Serial.begin(9600);
}

int stime = 5000;
void loop() {
    digitalWrite(out_pin,HIGH); 
    delay(stime); 
    digitalWrite(out_pin,LOW); 
    delay(stime); 
}
