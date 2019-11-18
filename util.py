import serial
from pythonosc.osc_message_builder import OscMessageBuilder
from pythonosc import udp_client
import time

class Serial_Controller:
    def __init__(self, tty, baud):
        print("Serial Setup....", end="")
        self.ser = serial.Serial(tty, baud, timeout=1)
        time.sleep(5)
        print("Serial Setup Done")
    
    def send_msg(self, msg):
        print("[INFO] Send ...", msg)
        self.ser.write(msg)


class Osc_Handler:
    def __init__(self, ip, port, address):
        print("Osc Setup....", end="")
        self.client = udp_client.UDPClient(ip, port) 
        self.address = address
        print("Osc Done")

    def send(self, signal):
        msg = OscMessageBuilder(address=self.address)
        for i in range(len(signal)):
            msg.add_arg(signal[i])
        m = msg.build()
        try:
            self.client.send(m)
        except:
            print("osc error..")