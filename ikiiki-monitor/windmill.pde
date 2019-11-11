
class Windmill {

    int x, y;
    boolean bRotating;
    
    Windmill() {

    }

    void setPos(int _x, int _y) {
        x = _x;
        y = _y;
    }

    void draw() {
        push();
        translate(x, y);
        
    }
};