int pinarray[3] = {8, 9, 10};
int winds = 0;
int winds_array[3] = {0, 0, 0};
bool state = false;
int winds_num = sizeof(winds_array);

void action() {
    for(int i=0; i<winds_num; i++){
        if(winds_array[i] > 0)
            digitalWrite(pinarray[i], 1);
        else
            digitalWrite(pinarray[i], 0);
    }
    // Serial.print(winds_array);
}

void set_winds() {
    if(winds < 3 && state)
        return;
    for(int i=winds_num-1; i>0; i--) {
        winds_array[i] = winds_array[i-1];
    }
    winds_array[0] = winds;
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
                winds += 1;
                state = true;
                break;
            case 'b':
                winds -= 1;
                state = false;
                break;
        }
    }
}
