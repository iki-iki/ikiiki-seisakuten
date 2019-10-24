import time
import grovepi
import serial

TTY = "/dev/ttyUSB0"
BAUD = 115200 

# HIGH : black 
# LOW : white 

class Send_Serial:
    def __init__(self, tty, baud):
        self.ser = serial.Serial(tty, baud, timeout=0.1)
        self.sensor_pin = 4
        grovepi.pinMode(self.sensor_pin, "INPUT")
        self.prev = 0
        self.stop_time = time.time()
        self.stop_duration = 3
        self.state_change = True
    
    def main(self):
        while True:
            s = grovepi.digitalRead(self.sensor_pin)
            v = self.judge(s)
            self.send_msg(v)            
            time.sleep(.01)

    def send_msg(self, value):
        if value is 1:
            msg = b"a"
        elif value is 0:
            msg = b"b"
        elif value is -1:
            return
        self.ser.write(msg)

    def judge(self, s):
        print(self.prev, " -> ", s)
        if s != self.prev:
            v = 1
            print("start")
            self.state_change = 1
        else:
            v = -1
            if self.state_change == 1:
                self.stop_time = time.time()
            duration = time.time() - self.stop_time
            if duration > self.stop_duration + 0.5:
                v = -1
            elif duration > self.stop_duration:
                v = 0
                print("stop")
            self.state_change = 0
        self.prev = s 
        return v
        

s = Send_Serial(TTY, BAUD)
s.main()