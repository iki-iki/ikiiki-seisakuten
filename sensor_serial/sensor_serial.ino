int photo_pin = 1;

void setup() {
    Serial.begin(9600);
}

void loop() {
    int s = analogRead(photo_pin);
    // uint8_t val = (uint8_t)(s/4);
    String send = String(s);
    // String send = "hello world";
    Serial.println(send);
    // Serial.print(" ");
    // Serial.println(val);
    // byte msg = byte(s);
    // Serial.write(msg);
    // Serial.write("\n");
    // Serial.write("hello\n");

    delay(10);
}
