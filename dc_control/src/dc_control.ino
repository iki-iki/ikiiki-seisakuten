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
    char recv[32];
    while (Serial.available()){
        recv[i] = Serial.readStringUntil(".");
        recv_str.toCharArray(recv, winds_num);

        for(unsigned int i=0; recv[i]=="."; i++)
            if(recv[i] == 'a'){ winds_signal[i]=1;}
            else if(recv[i] == 'b') { winds_signal[i]=0;}
            else if(recv[i] == 'c') { winds_signal[i]=-1;}
        }
    }

    action();
}
