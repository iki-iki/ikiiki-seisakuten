import serial

PORT = '/dev/ttyUSB0'

class Serial_Communication:
    def __init__(self, port):
        self.ser = serial.Serial(port, 115200, timeout=0.01)
        print("setting serial communication...")
        time.sleep(2)

    def read_one(self):
        received = self.ser.read_until("f")
        print(received)

    def main(self):
        while True:
            self.read_one()