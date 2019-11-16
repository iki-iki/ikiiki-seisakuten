from queue import Queue
# from calc import Windmill_Calculator
from calc2 import Wind_Operator
from wm import WindMill

# cm
WINDMILL_POSITIONS = [
    [20, 160], [25, 130], [35, 150], 
    [40, 120], [50, 135], [70, 150], 
    [35, 100], [59, 108], [70, 125],
    [87, 140], [45, 70],  [85, 110],
    [110, 135],[50, 50],  [75, 75],
    [113, 98], [135, 130],[72, 40],
    [105, 70], [145, 110],[75, 15],
    [96, 42],  [140, 85], [102, 20],
    [113, 36], [128, 58], [165, 70],
    [170, 85], [130, 30], [150, 50]
]


class Windmill_Controller:
    def __init__(self):
        self.windmill_num = len(WINDMILL_POSITIONS)
        self.windmills = []
        # init winds value
        for i in range(self.windmill_num):
            self.windmills.append(WindMill(WINDMILL_POSITIONS[i], i+1))
        # self.calculator = Windmill_Calculator(self.windmills)
        self.calc = Wind_Operator()
        self.loop_index = 0

    def create_msg(self, bRotatings):
        print(bRotatings)
        self.calc.handle_new_winds(bRotatings)
        winds_list = self.calc.get_winds_place()
        for i in range(self.windmill_num):
            self.windmills[i].set_signal(bool(winds_list[i]))
        strmsg = self.array_to_str(winds_list)
        self.loop_index += 1
        if self.loop_index % 100 is 0:
            self.calc.changeMode()
        return strmsg

    def create_msg_demo(self, bRotatings):
        print(bRotatings)
        if True in bRotatings:
            for i in range(30):
                self.windmills[i].set_signal(True)
        else:
            for i in range(30):
                self.windmills[i].set_signal(False)
        signals = self.get_signal()
        strmsg = self.array_to_str(signals)
        return strmsg


    # bRotatings : array of sensor flag
    # def gen_msg(self, bRotatings):
    #     print('calc')
    #     self.calculator.calc(bRotatings)
    #     msg = self.get_signal() 
    #     strmsg = self.array_to_str(msg)
    #     self.loop_index += 1
    #     if self.loop_index % 100 is 0:
    #         self.calculator.changeMode()
    #     return strmsg

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

    def get_signal(self):
        msg =[]
        for i in range(self.windmill_num):
            msg.append(self.windmills[i].signal)
        return msg
    
    def get_states(self):
        states = []
        for i in range(self.windmill_num):
            states.append(self.windmills[i].bRotating)
        return states