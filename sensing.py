# HIGH : black 
# LOW : white 

import grovepi
import time
import random

class Sensor:
    def __init__(self, _pin):
        self.pin = _pin 
        self.val = 0
        self.pre_val = 0
        self.bRotating = False
        self.bStopping = False
        self.stop_interval = 3.5 
        self.stop_time = time.time() 
        grovepi.pinMode(self.pin, "INPUT")

    def read_value(self):
        self.pre_val = self.val
        self.val = grovepi.digitalRead(self.pin)
        # r = random.random()
        # self.val = 1 if r > 0.7 else 0

    def judge_if_rotating(self):
        if self.val != self.pre_val: # get state change
            # print("Rotating")
            self.bRotating = True
            self.bStopping = False
        else: # if state not changes
            if self.bRotating is True and self.bStopping is False:
                # print("Record Stopping Time")
                self.stop_time = time.time()
                self.bStopping = True
            else:
                duration = time.time() - self.stop_time
                # print("Duration :", duration)
                if duration > self.stop_interval and duration < 10000:
                    self.bRotating = False
                    self.bStopping = False
                else:
                    self.bRotating = True
                    self.bStopping = True
 
class Sensor_Handler:
    def __init__(self):
        self.pins = [2, 3, 4]
        self.sensors = []
        for i in range(len(self.pins)):
            self.sensors.append(Sensor(self.pins[i]))
            
    def judge_if_rotating(self):
        for i in range(len(self.pins)):
            self.sensors[i].read_value()
            self.sensors[i].judge_if_rotating()
        rot = self.get_rotatings() 
        # print(rot, end="")

    def get_flags(self):
        flags = []
        for i in range(len(self.pins)):
            flags.append(self.sensors[i].bRotating)
        return flags

    def get_rotatings(self):
        rotatings = []
        for i in range(len(self.pins)):
            rotatings.append(self.sensors[i].val)
        return rotatings

if __name__ == '__main__':
    sh = Sensor_Handler()
    while True:
        try:
            sh.judge_if_rotating()
            sflag = []
            for i in range(3):
                sflag.append(sh.sensors[i].val)
            print("bval", sflag)
            flag = sh.get_flags()
            print("flag",flag)
            time.sleep(.1)
        except KeyboardInterrupt:
            break