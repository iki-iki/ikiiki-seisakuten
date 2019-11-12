int pinarray[] = {22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51};
int winds_num = 30;

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
