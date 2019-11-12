
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
            fill(150, 100);
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
        if(bWinding) fill(255);
        else fill(10);
        String c = "S" + str(index);
        float cw = textWidth(c);
        text(c, x-cw/2, y);
    }
};