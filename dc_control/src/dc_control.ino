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
    char recv[30];
    unsigned char i = 0;
    while (Serial.available()){
        recv[i] = Serial.read();

        if(i>winds_num || recv[i] == "."){
            break;
        } else {
            if(recv[i] == 'a'){ winds_signal[i]=1;
            else if(recv[i] == 'b') { winds_signal[i]=0;}
            else if(recv[i] == 'c') { winds_signal[i]=-1;}
            i++;
        }
    }

    action();
}
