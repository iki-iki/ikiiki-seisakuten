import time
import serial

tty = "COM7"
baud = 115200
ser = serial.Serial(tty, baud, timeout=0.1)

while True:
    c = b"a"
    ser.write(c)
    print("write a")
    time.sleep(3)
    c = b"b"
    ser.write(c)
    print("write b")
    time.sleep(3)
