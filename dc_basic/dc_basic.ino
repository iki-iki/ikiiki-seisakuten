int out_pin = 13;

void setup() {
    pinMode(out_pin, OUTPUT);
    Serial.begin(115200);
}

// int signal;
// void loop() {
//     signal = 1;
//     digitalWrite(out_pin, signal);
//     delay(1000);
//     signal = 0;
//     digitalWrite(out_pin, signal);
//     delay(1000);
// }

// String a;
// void loop() {
    // while(Serial.available()) {
        // char inputchar;
        // inputchar = Serial.read();
        // Serial.println(inputchar);
        // a = Serial.readStringUntil("\n");
        // if(a == "a") {
        // if(inputchar == 'a'){
            // digitalWrite(out_pin, HIGH);
            // Serial.println("char a");
        // } else if(inputchar == 'b') {
            // digitalWrite(out_pin, LOW);
            // Serial.println("char b");
        // }
    // }
// }

void loop() {
    String recv_str;
    char recv[30];
    while (Serial.available()){
        recv_str = Serial.readStringUntil(".");
        Serial.println(recv_str);
        recv_str.toCharArray(recv, 32);
        int str_len = recv_str.length()-1;
        for(unsigned int i=0; i<str_len; i++){
            String ss;
            ss = recv_str.charAt(i);
            Serial.println(ss);
            if(!ss.compareTo("a")){
                Serial.println("same a");
            }
            else if(!ss.compareTo("b")){
                Serial.println("same b");
            }
        }
    }
}
