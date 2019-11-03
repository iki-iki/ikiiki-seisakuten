
class WindMill:
    def __init__(self, _pos):
        self.pos = _pos
        self.bRotating = False
        self.send_signal = -1


class Windmill_Calculator:
    def __init__(self, windmills):
        self.windmills = windmills
        self.wind_mode = 0

    def calc(self):
        if 