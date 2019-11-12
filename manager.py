import time
import threading
from windmill import Windmill_Controller
from util import Serial_Controller, Osc_Handler
from sensing import Sensor_Handler 


class Manager:
    def __init__(self, tty, baud):
        self.serialController = Serial_Controller(tty, baud)
        self.SH = Sensor_Handler()
        self.WC = Windmill_Controller()
        self.OC = Osc_Handler("127.0.0.1", 1234, '/windmill')

    def thread_init(self):
        self.t1 = threading.Thread(target=self.t1)
        self.t2 = threading.Thread(target=self.t2)
        self.t1.start()
        self.t2.start()
    
    def t1(self):
        while True:
            self.read_input()
            time.sleep(.1)

    def read_input(self):
        self.SH.judge_if_rotating()

    def t2(self):
        while True:
            self.serial_output()
            time.sleep(1)
    
    def serial_output(self):
        msg = self.WC.gen_msg(self.SH.get_flags())            
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
