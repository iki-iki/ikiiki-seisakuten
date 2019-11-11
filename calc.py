
class WindMill:
    def __init__(self, _pos):
        self.pos = _pos
        self.bRotating = False
        self.signal = -1 # 1(on), 0(off), -1(stay)
        

class Windmill_Calculator:
    def __init__(self, windmills):
        self.windmills = windmills  # set windmill array pointer
        self.wind_mode = 0

    # bRotatings : array of sensor flag
    # no need to return value
    # set signal value for each windmill class
    def calc(self, bRotatings):
        if self.wind_mode is 0:
            self.eradiation()

    def eradiation(self):
        