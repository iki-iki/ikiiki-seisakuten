
class Sensor {

    int x, y;
    boolean bWinding = false;
    int index;
    int drawsize = 15;

    Sensor(int _x, int _y) {
        x = _x;
        y = _y;
    }

    void setIndex(int i) {
        index = i;
    }

    void drawInScale(float scale) {
        int xx = int(x*scale); int yy = int(y*scale);
        
        if (bWinding){
            color(255, 0, 0);
            noStroke();
        } else {
            fill(255);
            noStroke();
        }

        int ds = int(drawsize * scale);
        rect(xx-ds/2, yy-ds/2, ds, ds);
        drawIndex(xx, yy);

    }

    void drawIndex(int x, int y) {
        textSize(20);
        fill(10);
        text("S"+str(index), x, y);
    }

};