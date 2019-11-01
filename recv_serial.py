import serial
import time
import re
import binascii

PORT = '/dev/ttyUSB0'

class Serial_Communication:
    def __init__(self, port):
        self.ser = serial.Serial(port, 9600, timeout=0.01)
        print("setting serial communication...")
        time.sleep(2)

    def read_one(self):
        recv = self.ser.readline()
        value = recv.decode('ascii', errors="ignore")
        if len(value) is not 0:
            v = int(value)
            print(v)


    def main(self):
        while True:
            self.read_one()

sc = Serial_Communication(PORT)
sc.main()