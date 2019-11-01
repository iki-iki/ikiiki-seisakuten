from queue import Queue

class Windmill_Calc:
    def __init__(self):
        self.windmill_num = 3
        # init winds value
        self.distance = [2, 4, 6] 
        self.last_signal = 0 
        self.winds = []
        self.last_message = []
        for i in range(len(self.windmill_num)):
            self.winds.append(Queue())
            self.last_message.append(-1)
            
    def get_msg(self, signal):
        self.calc(signal)
        msg = []
        for i in range(self.windmill_num):
            s = self.winds[i].get()
            if self.last_signal is s:
                msg.append(-1) 
            elif self.last_signal is 1 and s is 0:
                msg.append(0)
            elif self.last_signal is 0 and s is 1:
                msg.append(1)
        strmsg = self.array_to_str(msg)
        print("[INFO]Send Msg ...", strmsg)
        return strmsg 

    def array_to_str(self, a):
        s = b""
        for i in range(self.windmill_num):
            if a[i] is 1:
                s += b"a"
            elif a[i] is 0:
                s += b"b"
            elif a[i] is -1:
                s += b"c"
        s += b"."
        return s

    
    # 1 : start, 0: stop, -1: keep
    def calc(self, signal):
        if signal is -1:
            for k in range(self.windmill_num):
                self.winds[k].put(self.last_signal)
            return

        for i in range(self.windmill_num):
            for _ in range(self.distance[i]):
                self.winds[i].put(int(not(signal)))
            self.winds[i].put(signal)
        self.last_signal = signal
