

class Windmill_Calculator:
    def __init__(self, windmills):
        self.windmills = windmills  # set windmill array pointer
        self.wind_mode = 0

    # bRotatings : array of sensor flag
    # no need to return value
    # set signal value for each windmill class
    def calc(self, bRotatings):


    def changeMode(self):
        self.wind_mode += 1
        if self.wind_mode is 3:
            self.wind_mode = 0