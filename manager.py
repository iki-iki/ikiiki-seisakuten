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

    def main(self):
        self.read_input()
        if time.time() - self.t > 2:
            self.serial_output()
            self.t = time.time()
            
    def read_input(self):
        self.SH.judge_if_rotating()

    def serial_output(self):
        # msg = self.WC.gen_msg(self.SH.get_flags())            
        msg = self.WC.create_msg(self.SH.get_flags())
        self.serialController.send_msg(msg)
        self.send_osc_message()

    def send_osc_message(self):
        info = []
        sensors = self.SH.get_flags()
        windmills = self.WC.get_states()
        t = sensors + windmills
        t = list(map(int, t))
        print("SendOsc", t)
        self.OC.send(t)
