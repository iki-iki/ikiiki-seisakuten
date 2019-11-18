import time
import datetime
from windmill import Windmill_Controller
from util import Serial_Controller, Osc_Handler
from sensing import Sensor_Handler 

class Manager:
    def __init__(self, tty, baud):
        print("Manager INIT")
        self.serialController = Serial_Controller(tty, baud)
        self.SH = Sensor_Handler()
        self.WC = Windmill_Controller()
        self.OC = Osc_Handler("157.82.207.244", 1234, '/windmills')
        self.t = time.time()
        self.sensing_hist = [False, False, False]
        self.serial_send_interval = 1.0 
        print("Manager Setup DONE")

    def main(self):
        sensors = self.read_input()
        self.append_sensing_history(sensors)
        if time.time() - self.t > self.serial_send_interval:
            self.serial_output()
            self.t = time.time()
            self.reset_sensing_history()
    
    def append_sensing_history(self, ss):
        for i, s in enumerate(ss):
            if s is True:
                self.sensing_hist[i] = True

    def reset_sensing_history(self):
        self.sensing_hist.clear()
        self.sensing_hist = [False, False, False]
            
    def read_input(self):
        self.SH.judge_if_rotating()
        sensors = self.SH.get_flags()
        return sensors

    def serial_output(self):
        # msg = self.WC.gen_msg(self.sensing_hist)            
        msg = self.WC.create_msg(self.sensing_hist)
        # msg = self.WC.create_msg_demo(self.sensing_hist)
        # msg = b"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        # msg = b"bbbbbbbbbbbbbbbaaaaaaaaaaaaaaa"
        if b"a" in msg or b"b" in msg:
            print(datetime.datetime.now())
            self.serialController.send_msg(msg)
            self.send_osc_message()
        elif type(msg) is not bytes:
            print("msg is no String", msg)

    def send_osc_message(self):
        info = []
        sensors = self.SH.get_flags()
        windmills = self.WC.get_states()
        t = sensors + windmills
        t = list(map(int, t))
        print("SendOsc", t)
        self.OC.send(t)
