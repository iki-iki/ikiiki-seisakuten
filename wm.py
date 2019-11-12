# eradiation, clock, counterclock
# S1: 31, S2: 32, S3: 33
WINDMILL_RELATION = [
    [[31],        [31,3],    [31,2]], # 1
    [[],          [1,3],     [7]],    # 2
    [[1],         [1,6],     [1,4]],  # 3
    [[3,8],       [2,5],     [7]],    # 4
    [[3],         [6],       [3]],    # 5
    [[],          [10],      [3]],    # 6
    [[8],         [4],       [11]],   # 7
    [[4,5,12],    [4],       []],     # 8
    [[4,5,12],    [],        []],     # 9
    [[12],        [13],      [6]],    # 10
    [[15],        [7],       [14]],   # 11
    [[8,9,15,16], [],        []],     # 12
    [[12],        [17],      [10]],   # 13
    [[15],        [11],      [18]],   # 14
    [[12, 18, 19],[8],       []],     # 15
    [[12, 19, 23],[],        []],     # 16
    [[16],        [20],      [13]],   # 17
    [[21],        [14,15],   [21,22]],# 18
    [[15,16,22,23],[],       []],     # 19
    [[],          [23,28,33],[17]],   # 20
    [[32],        [18,32],   [24,32]],# 21
    [[19, 21],    [18],      [25]],   # 22
    [[28],        [26],      [20]],   # 23
    [[22],        [21,32],   [25, 29]],#24
    [[22],        [22,24],   [26]],   # 25
    [[19],        [25],      [23,27]],# 26
    [[],          [30],      [28]],   # 27
    [[33],        [27,23,33],[20,33]],# 28
    [[25],        [25,24],   [30]],   # 29
    [[26],        [29],      [27]],   # 30
]

class WindMill:
    def __init__(self, _pos, index):
        self.pos = _pos
        self.bRotating = False
        self.signal = -1 # 1(on), 0(off), -1(stay)
        self.prev_rotating = False
        self.index = index

    def changeMode(self):
        self.mode += 1
        if self.move is 3:
            self.move = 0

    def get_read_pins(self, mode):
        return WINDMILL_RELATION[self.index-1][mode]
        
    def next_rotating(self, pinsaround):
        if len(pinsaround) is 0:
            return 0
        if 1 in pinsaround:
            return 1
        else:
            return 0
            

    def set_signal(self, rotating):
        self.prev_rotating = self.bRotating
        if rotating == self.prev_rotating:
            self.signal = -1
        else:
            self.signal = rotating
