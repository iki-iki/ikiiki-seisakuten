import time
import threading
import grovepi
import serial
from Windmill_Controller import Windmill_Controller

TTY = "/dev/ttyUSB0"
BAUD = 115200 

# HIGH : black 
# LOW : white 

class Sensor:
    def __init__(self, _pin, _pos):
        self.pin = _pin 
        self.val = 0
        self.pre_val = 0
        self.bRotating = False
        self.stop_interval = 0.5
        grovepi.pinMOde(self.pin, "INPUT")

    def read_value(self):
        self.val = grovepi.digitalRead(self.pin)

    def judge_if_rotating(self):
        if self.val != self.pre_val: # get state change
            self.bRotating = True
            print("[INFO]start wind")
        else: # if state not changes
            if self.bRotating is True:
                print("[INFO]stopping")
            else:
                duration = time.time() - self.stop_interval
                if duration > self.stop_interval:
                    self.bRotating = False
                    print("[INFO]stopped")
                else:
                    self.bRotatings = True
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
    

class Serial_Controller:
    def __init__(self, tty, baud):
        print("Serial Setup....")
        self.ser = serial.Serial(tty, baud, timeout=1)
        time.sleep(5)
    
    def send_msg(self, msg):
        print("[INFO] Send ...", msg)
        self.ser.write(msg)

class Send_Serial:
    def __init__(self, tty, baud):
        self.serialController = Serial_Controller(tty, baud)
        self.SH = Sensor_Handler()
        self.WC = Windmill_Controller()
        self.bRotatings = [False, False, False]
        self.t1 = threading.Thread(target=self.read_input)
        self.t2 = threading.Thread(target=self.serial_output)
        self.t2_duration = 1.0
        self.t2_time = 0
        self.t1.start()
        self.t2.start()
    
    def main(self):
        self.t1.join()
        self.t2.join()
    
    def read_input(self):
        self.SH.judge_if_rotating()
    
    def serial_output(self):
        now = time.time()
        if now - self.t2_time < self.t2_duration:
            return
        self.t2_time = now
        msg = self.WC.gen_msg(self.SH.sensors)            
        self.serialController.send_msg(msg)


s = Send_Serial(TTY, BAUD)
s.main()