import time
import grovepi
import serial
from windmill_calc import Windmill_Calc

TTY = "/dev/ttyUSB0"
BAUD = 115200 

# HIGH : black 
# LOW : white 
# switchしたいときだけシグナルを送る

class Send_Serial:
    def __init__(self, tty, baud):
        # init serial
        self.ser = serial.Serial(tty, baud, timeout=0.1)
        # init sensor settings
        self.sensor_pin = 4
        grovepi.pinMode(self.sensor_pin, "INPUT")
        self.prev = 0
        # init variables
        self.stop_time = time.time()
        self.stop_duration = 3
        self.state_change = False
        self.state = False
        # init calculator
        self.WC = Windmill_Calc()
    
    def main(self):
        while True:
            s = grovepi.digitalRead(self.sensor_pin)
            v = self.judge_wind(s)
            # 1 : start 0: stop -1 : keep
            msg = self.WC.calc(v)            
            self.send_msg(msg)
            time.sleep(.01)

    def send_msg(self, msg):
        print("[INFO] send ...", msg)
        self.ser.write(msg)

    def judge_wind(self, s):
        # print(self.prev, " -> ", s)
        if s != self.prev: # get state change
            v = 1
            self.state = True
            print("[INFO]start wind")
            if s is 0:
                self.stop_time = time.time()
                print("[INFO]Set Stop Time")
        else: # if state not changes
            v = -1
            duration = time.time() - self.stop_time
            if self.state and s is 0 and duration > self.stop_duration + 0.5:
                v = 0
                self.state = False
                print("[INFO]stop wind")
            self.state_change = 0
        # record current state
        self.prev = s 
        return v
        

s = Send_Serial(TTY, BAUD)
s.main()