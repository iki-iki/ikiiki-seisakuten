int pinarray[3] = {8, 9, 13};

void action(int signal) {
    for(int i=0; i<sizeof(pinarray); i++){
        digitalWrite(pinarray[i], signal);
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

        switch(inputchar){
            case 'a':
                action(1);
                break;
            case 'b':
                action(0);
                break;
        }
    }
}
