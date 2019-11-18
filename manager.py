import time
from windmill import Windmill_Controller
from util import Serial_Controller, Osc_Handler
from sensing import Sensor_Handler 

class Manager:
    def __init__(self, tty, baud):
        self.serialController = Serial_Controller(tty, baud)
        self.SH = Sensor_Handler()
        self.WC = Windmill_Controller()
        self.OC = Osc_Handler("157.82.207.244", 1234, '/windmills')
        self.t = time.time()
        self.sensing_hist = [False, False, False]
        self.serial_send_interval = 1.0 

    def main(self):
        self.read_input()
        sensors = self.SH.get_flags()
        for i, s in enumerate(sensors):
            if s is True:
                self.sensing_hist[i] = True
        if time.time() - self.t > self.serial_send_interval:
            self.serial_output()
            self.t = time.time()
            self.reset_sensing_history()

    def reset_sensing_history(self):
        self.sensing_hist.clear()
        self.sensing_hist = [False, False, False]
            
    def read_input(self):
        self.SH.judge_if_rotating()

    def serial_output(self):
        # msg = self.WC.gen_msg(self.sensing_hist)            
        msg = self.WC.create_msg(self.sensing_hist)
        # msg = self.WC.create_msg_demo(self.sensing_hist)
        # msg = b"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        # msg = b"bbbbbbbbbbbbbbbaaaaaaaaaaaaaaa"
        if b"a" in msg or b"b" in msg:
            self.serialController.send_msg(msg)
            self.send_osc_message()

    def send_osc_message(self):
        info = []
        sensors = self.SH.get_flags()
        windmills = self.WC.get_states()
        t = sensors + windmills
        t = list(map(int, t))
        print()
        print("SendOsc", t)
        self.OC.send(t)
