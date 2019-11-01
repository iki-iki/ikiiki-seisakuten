int pinarray[] = {9, 8, 10, 13};
int winds_num = sizeof(pinarray);
int winds_signal[4];

void action() {
    for(int i=0; i<winds_num; i++){
        if(winds_signal[i] == -1) 
            continue;
        digitalWrite(pinarray[i], winds_signal[i]);
    }
}

void setup() {
    for(int i=0; i<winds_num; i++) {
        pinMode(pinarray[i], OUTPUT);
        winds_signal[i] = 0;
    }
    Serial.begin(115200);
    
}

void loop() {
    String recv_str;
    while (Serial.available()){
        recv_str = Serial.readStringUntil(".");
        int str_len  recv_str.length() - 3;
        for(unsigned int i=0; i<str_len; i++){
            String ss;
            ss = recv_str.charAt(i);
            if(!ss.compareTo("a")){ winds_signal[i]=1;}
            else if(ss.compareTo("b")) { winds_signal[i]=0;}
            else if(ss.compareTo("c")) { winds_signal[i]=-1;}
        }
    }

    action();
}
