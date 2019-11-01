int pinarray[] = {9, 8, 10, 13};
int winds_num = sizeof(pinarray);
int winds_signal[];

void action() {
    for(int i=0; i<winds_num; i++){
        if(winds_signal[i] == -1) 
            continue;
        digitalWrite(pinarray[i], winds_signal[i]);
    }
}

void setup() {
    for(int i=0; i<sizeof(pinarray); i++) {
        pinMode(pinarray[i], OUTPUT);
    }
    Serial.begin(115200);
    
}

void loop() {
    while (Serial.available()){
        int inputchar = Serial.read();

        if(inputchar[0] == "a") { winds_signal[0] = 1; }
        else if(inputchar[0] == "b") { winds_signal[0] = 0; }
        else if(inputchar[0] == "c") { winds_signal[0] = -1; }
    }
    action();
}
