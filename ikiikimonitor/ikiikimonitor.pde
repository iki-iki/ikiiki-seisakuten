import oscP5.*;
import netP5.*;

float view_scale = 5.5;
Manager m;

OscP5 oscP5;

void setup() {
    m = new Manager(view_scale);
    m.setup();
    size(1200, 1200);
    background(30, 100);

    oscP5 = new OscP5(this, 1234);
}


void draw() {
    m.update();
    m.draw();
}

void oscEvent(OscMessage msg) {
    if(msg.checkAddrPattern("/windmills")){
        for(int i=0; i<33; i++) {
            int s = msg.get(i).intValue();
            m.signals[i] = s; 
        }
    }
}