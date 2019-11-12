# HIGH : black 
# LOW : white 

import grovepi
import time

class Sensor:
    def __init__(self, _pin, _pos):
        self.pin = _pin 
        self.val = 0
        self.pre_val = 0
        self.bRotating = False
        self.stop_interval = 0.5
        grovepi.pinMode(self.pin, "INPUT")

    def read_value(self):
        self.val = grovepi.digitalRead(self.pin)

    def judge_if_rotating(self):
        if self.val != self.pre_val: # get state change
            self.bRotating = True
            print("[INFO]start wind")
        else: # if state not changes
            if self.bRotating is True:
                pass
            else:
                duration = time.time() - self.stop_interval
                if duration > self.stop_interval:
                    self.bRotating = False
                else:
                    self.bRotating = True
                    print("[INFO]stopping....")
        # record current state
        self.pre_val = self.val 
 
class Sensor_Handler:
    def __init__(self):
        self.pins = [2, 3, 4]
        self.positions = [[0, 0], [10, 0], [0, 10]]
        self.sensors = []
        for i in range(len(self.pins)):
            self.sensors.append(Sensor(self.pins[i], self.positions))
            
    def judge_if_rotating(self):
        for i in range(len(self.pins)):
            self.sensors[i].read_value()
            self.sensors[i].judge_if_rotating()

    def get_flags(self):
        flags = []
        for i in range(len(self.pins)):
            flags.append(self.sensors[i].bRotating)
        return flags
