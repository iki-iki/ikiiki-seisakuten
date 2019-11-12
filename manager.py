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
        self.OC = Osc_Handler("127.0.0.1", 12345, '/windmill')

    def thread_init(self):
        self.t1 = threading.Thread(target=self.read_input)
        self.t2 = threading.Thread(target=self.serial_output)
        self.t2_duration = 1.0
        self.t2_time = 0
        self.t1.start()
        self.t2.start()
    
    def main(self):
        while True:
            try:
                self.t1.join(1)
                self.t2.join(1)
            except:
                self.t1.stop()
                self.t2.stop()
        print("=========PROGRAM FINISHED")
    
    def read_input(self):
        self.SH.judge_if_rotating()
    
    def serial_output(self):
        now = time.time()
        if now - self.t2_time < self.t2_duration:
            return
        self.t2_time = now
        msg = self.WC.gen_msg(self.SH.get_flags())            
        self.serialController.send_msg(msg)
        self.send_osc_message()

    def send_osc_message(self):
        info = []
        sensors = self.SH.get_flags()
        windmills = self.WC.get_signal()
        t = sensors + windmills
        t = map(int, t)
        self.OC.send(list(t))
