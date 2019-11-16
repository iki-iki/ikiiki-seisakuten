import time
import serial

PORT = "/dev/ttyACM0"
print("Serial Connecting...")
ser = serial.Serial(PORT, 115200, timeout=1)
time.sleep(5)

def get_sleep_sig():
    signal = ""
    for i in range(30):
        signal += "b"
    signal = signal.encode()
    return signal

def create_sig_without(ind):
    signal = ""
    for i in range(30):
        if i is ind:
            signal += "b"
        else:
            signal += "a"
    signal = signal.encode()
    return signal


def create_sig(ind_from, ind_to):
    signal = ""
    for i in range(30):
        # if i is ind:
        if i < ind_to and i >= ind_from:
        # if i > ind:
            signal += "a"
        else:
            signal += "b"
    signal = signal.encode()
    return signal

def send_for_each(ind_from, ind_to):
    signal = create_sig(ind_from, ind_to)
    print("for each", ind_from, "-", ind_to, signal)
    send_msg(signal)
    # print(ser.readline())
    # print(ser.readline())
    # print(ser.readline())
    time.sleep(1)

ok = [0, 1, 5, 9, 10, 12, 13, 14, 17, 20, 21]

def wind_from_list(w):
    m = ""
    ok_ind = 0
    for i in range(30):
        if ok_ind >= len(w):
            m += "b"
        elif i is w[ok_ind]:
            m += "a"
            ok_ind += 1
        else:
            m += "b"
    msg = m.encode()
    send_msg(msg)

def send_msg(msg):
    ser.write(msg)
    print("write", msg)
    # print(ser.readline())
    # print(ser.readline())
    # print(ser.readline())
    time.sleep(1)
while True:
    try:
        for i in range(30):
            send_for_each(0, i)
            time.sleep(3)
        # for i in range(6):
        # for i in ok:
        # msg = create_sig_without(4)
        # send_msg(msg)
        # send_for_each(0, 30)
        # wind_from_list(ok)
        # time.sleep(15)
        sig = get_sleep_sig()
        send_msg(sig)
        time.sleep(3)
    except KeyboardInterrupt:
        break
    # send_for_e1ch(29)
    # send_for_each(29)
    # m = get_sleep_sig()
    # send_msg(m)

ser.close()