import time
import serial

print("Serial Connecting...")
ser = serial.Serial('COM7', 115200, timeout=1)
time.sleep(5)

signals = [b"aaaa", b"bbbb", b"cccc"]

def send_signal(sig_ind):
    signal = signals[sig_ind]
    ser.write(signal)
    print("write", signal)
    print(ser.readline())
    print(ser.readline())
    print(ser.readline())
    time.sleep(1)

for i in range(4):
    send_signal(0)
    send_signal(2)
    send_signal(2)
    send_signal(1)
    send_signal(2)
    send_signal(2)

ser.close()