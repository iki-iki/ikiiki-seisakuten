
class Windmill {

    int x, y;
    boolean bRotating = false;
    int r;
    int index;
    
    Windmill(int _x, int _y, int _r) {
        x = _x;
        y = _y;
        r = _r;
    }

    void setPos(int _x, int _y) {
        x = _x;
        y = _y;
    }

    void setR(int _r) {
        r = _r;
    }

    void setIndex(int _i){
        index = _i;
    }

    void drawInScale(float scale) {
        int xx = int(x*scale); int yy = int(y*scale);
        
        if (bRotating){
            fill(255,0,0,150);
            noStroke();
        } else {
            fill(255);
            noStroke();
        }

        int rr = int(r*scale);
        ellipse(xx, yy, rr, rr);
        drawIndex(xx, yy);

    }

    void drawIndex(int x, int y) {
        textSize(20);
        if(bRotating) fill(255);
        else fill(10);
        String c = str(index);
        float cw = textWidth(c);
        text(c, x-cw/2, y);
    }
};