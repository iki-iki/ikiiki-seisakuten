import oscP5.*;
import netP5.*;

float view_scale = 5.5;
Manager m;

OscP5 oscP5;

void setup() {
    m = new Manager(view_scale);
    m.setup();
    size(1200, 1200);
    background(100, 100);

    oscP5 = new OscP5(this, 12345);
}


void draw() {
    m.update();
    m.draw();
}

void oscEvent(OscMessage msg) {
    if(msg.checkAddrPattern("/windmills")){
        for(int i=0; i<33; i++) {
            m.signals[i] = msg.get(i).intValue();
        }
    }
}