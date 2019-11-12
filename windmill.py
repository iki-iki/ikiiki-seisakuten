from queue import Queue
from calc import WindMill, Windmill_Calculator

# cm
WINDMILL_POSITIONS = [
    [100, 100],
    [20, 20],
    [30, 30],
    [50, 50]
]


class Windmill_Controller:
    def __init__(self):
        self.windmill_num = len(WINDMILL_POSITIONS)
        self.windmills = []
        # init winds value
        for i in range(self.windmill_num):
            self.windmills.append(WindMill(WINDMILL_POSITIONS[i]))
        self.calculator = Windmill_Calculator(self.windmills)

    # bRotatings : array of sensor flag
    def gen_msg(self, bRotatings):
        self.calculator.calc(bRotatings)
        msg = self.flags() 
        strmsg = self.array_to_str(msg)
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

    def flags(self):
        msg =[]
        for i in range(self.windmill_num):
            msg.append(self.windmills[i].signal)
        return msg