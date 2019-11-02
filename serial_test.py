import time
import serial

with serial.Serial('COM7', 115200, timeout=1) as ser:
    
# ser.port = "COM7"
# ser.baud = 115200
# ser.setDTR(False)
# ser.open()

    time.sleep(5)
    ser.write(b"bbbb.")
    print("write b")
    print(ser.readline())
    time.sleep(1)
    ser.write(b"bbbb.")
    print("write b")
    print(ser.readline())
    time.sleep(1)
    ser.write(b"bbbb.")
    print("write b")
    print(ser.readline())
    time.sleep(1)
    ser.write(b"bbbb.")
    print("write b")
    print(ser.readline())
    time.sleep(1)

    time.sleep(1)
    ser.write(b"aaaa.")
    print("write a")
    print(ser.readline())


    # stime = 1 
    # for i in range(20):
    #     ser.write(b"aaaa")
    #     print("write a")
    #     time.sleep(stime)
    #     ser.write(b"bbbb")
    #     print("write b")
    #     time.sleep(stime)
    #     ser.write(b"cccc")
    #     print("write c")
    #     ser.write