int out_pin = 13;

void setup() {
    pinMode(out_pin, OUTPUT);
    Serial.begin(115200);
}

void loop() {
    String recv_str;
    // char recv[30];
    while (Serial.available()){
        recv_str = Serial.readStringUntil(".");
        // recv_str.toCharArray(recv, 32);
        int str_len = recv_str.length()-3;
        for(unsigned int i=0; i<str_len; i++){
            String ss;
            ss = recv_str.charAt(i);
            Serial.println(ss);
            // Serial.println(strcmp(recv[i], "a"));
            if(!ss.compareTo("a")){
                Serial.println("this is a");
            }
        }
    }
}
