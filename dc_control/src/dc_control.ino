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
        int str_len = recv_str.length() - 1;
        for(unsigned int i=0; i<str_len; i++){
            String ss;
            ss = recv_str.charAt(i);
            if(!ss.compareTo("a")){
                // winds_signal[i]=1;
                digitalWrite(pinarray[i], 1);
                // Serial.println(winds_signal[i]);
            } else if(!ss.compareTo("b")) {
                // winds_signal[i]=0;
                digitalWrite(pinarray[i], 0);
                // Serial.println(winds_signal[i]);
            }
        }
    }

    // action();
}
