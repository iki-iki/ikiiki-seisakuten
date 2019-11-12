 
class Manager {

    Windmill[] windmills;
    int sizes[] = {15, 20, 25, 30};
    int windmill_num;
    float view_scale;
    int[][] windmill_data =  {
            {20,  160, sizes[0]},  // 1
            {25,  130, sizes[0]},  // 2
            {35,  150, sizes[1]},  // 3
            {40,  120, sizes[0]},  // 4 
            {50,  135, sizes[1]},  // 5
            {70,  150, sizes[1]},  // 6
            {35,  100, sizes[1]},  // 7
            {59,  108, sizes[2]},  // 8
            {70,  125, sizes[0]},  // 9
            {87,  140, sizes[1]},  // 10
            {45,  70,  sizes[1]},  // 11
            {85,  110, sizes[2]},  // 12
            {110, 135, sizes[2]},  // 13
            {50,  50,  sizes[1]},  // 14
            {75,  75,  sizes[3]},  // 15
            {113, 98, sizes[3]},  // 16
            {130, 130, sizes[1]},  // 17
            {72,  40,  sizes[2]},  // 18
            {105, 70,  sizes[2]},  // 19
            {145, 110, sizes[1]},  // 20
            {75,  15,  sizes[1]},  // 21
            {96, 42,  sizes[1]},  // 22
            {130, 50,  sizes[1]},  // 23
            {102, 20,  sizes[0]},  // 24
            {113, 36,  sizes[0]},  // 25
            {130, 73,  sizes[2]},  // 26
            {155, 70,  sizes[0]},  // 27
            {168, 55,  sizes[0]},  // 28
            {130, 30,  sizes[1]},  // 29
            {150, 50,  sizes[1]},  // 30
        };

    int[][] sensor_positions = {
        {0, 180}, {70, -10}, {200, 90}
    };
    int sensor_num = 3;
    Sensor[] sensors;
    int[] signals;
    
    Manager(float scale) {
        windmill_num = 30;
        view_scale = scale;
        signals = new int[33];
        for(int i=0; i<33; i++) {
            signals[i] = 0;
        }
    }

    void setup() {
        windmills = new Windmill[windmill_num]; 
        for(int i=0; i<windmill_num; i++) {
            Windmill wm = new Windmill(windmill_data[i][0], windmill_data[i][1], windmill_data[i][2]);
            wm.setIndex(i+1);
            windmills[i] = wm;
        }
        sensors = new Sensor[sensor_num];
        for(int j=0; j<sensor_num; j++) {
            Sensor s = new Sensor(sensor_positions[j][0], sensor_positions[j][1]);
            s.setIndex(j+1);
            sensors[j] = s;
        }
    }

    void update() {
        int i;
        for(i=0; i<3; i++) {
            sensors[i].bWinding = boolean(signals[i]);
        }
        for(int j=0; j<30; j++) {
            windmills[j].bRotating = boolean(signals[i+j]);
        }
    }

    void draw(){
        push();
        // rotate(-45);
        translate(50, 100);
        for (Windmill wm : windmills) {
            wm.drawInScale(view_scale);
        }
        for (Sensor s : sensors) {
            s.drawInScale(view_scale);
        }
        pop();
        drawPlate();
    }

    void drawPlate() {
        push();
        noFill();
        stroke(20);
        rect(105, 95, 1000, 975);
        pop();
    }
    
};
