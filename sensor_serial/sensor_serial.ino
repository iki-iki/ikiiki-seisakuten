int photo_pin = 1;


void setup() {
    Serial.begin(115200);
}

void loop() {
    int s = analogRead(photo_pin);
    uint8_t val = (uint8_t)(s / 4);
    // Serial.println(s);
    // Serial.print(" ");
    // Serial.println(val);
    Serial.write(val + "f");
}
