
class WindMill:
    def __init__(self, _pos):
        self.pos = _pos
        self.bRotating = False
        self.send_signal = -1
        

class Windmill_Calculator:
    def __init__(self, windmills):
        self.windmills = windmills  # set windmill array pointer
        self.wind_mode = 0

    # bRotatings : array of flag
    def calc(self, bRotatings):
        if self.wind_mode is 0:
            self.eradiation()

    def eradiation(self):
        