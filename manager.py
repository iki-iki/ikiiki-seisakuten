import time
import threading
from windmill import Windmill_Controller
from util import Serial_Controller
from sensing import Sensor_Handler 


class Manager:
    def __init__(self, tty, baud):
        self.serialController = Serial_Controller(tty, baud)
        self.SH = Sensor_Handler()
        self.WC = Windmill_Controller()

    def thread_init(self):
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
        msg = self.WC.gen_msg(self.SH.flags)            
        self.serialController.send_msg(msg)