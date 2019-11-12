import time
import serial

PORT = "COM7"
print("Serial Connecting...")
ser = serial.Serial(PORT, 115200, timeout=1)
time.sleep(5)

signals = [b"aaaaa", b"bbbb", b"cccc"]

def create_signal(ind):
    signal = ""
    for i in range(30):
        if ind is 0:
            signal += "a"
        elif ind is 1:
            signal += "b"
        elif ind is 2:
            signal += "c"
    signal = signal.encode()
    return signal

def send_signal(sig_ind):
    signal = create_signal(sig_ind) 
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
    send_signal(2)
    send_signal(2)
    send_signal(1)
    send_signal(2)

ser.close()