int pinarray[] = {9, 8, 10, 13};
int winds_num = 4;

void setup() {
    for(int i=0; i<winds_num; i++) {
        pinMode(pinarray[i], OUTPUT);
    }
    Serial.begin(115200);

}

String recv_str;
void loop() {
    if (Serial.available() > 0){
        recv_str = Serial.readStringUntil(".");
        Serial.println(recv_str);
        int str_len = recv_str.length();
        for(unsigned int i=0; i<str_len; i++){
            String ss;
            ss = recv_str.charAt(i);
            if(!ss.compareTo("a")){
                digitalWrite(pinarray[i], 1);
                // Serial.println(pinarray[i]);
            } else if(!ss.compareTo("b")) {
                digitalWrite(pinarray[i], 0);
                // Serial.println(pinarray[i]);
            }
        }
    }

    // action();
}
