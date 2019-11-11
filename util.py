import serial

class Serial_Controller:
    def __init__(self, tty, baud):
        print("Serial Setup....")
        self.ser = serial.Serial(tty, baud, timeout=1)
        time.sleep(5)
    
    def send_msg(self, msg):
        print("[INFO] Send ...", msg)
        self.ser.write(msg)
