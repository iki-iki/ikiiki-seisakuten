

class Windmill_Calculator:
    def __init__(self, windmills):
        self.windmills = windmills  # set windmill array pointer
        self.wind_mode = 0
        self.sensor_info = []

    # bRotatings : array of sensor flag
    # no need to return value
    # set signal value for each windmill class
    def calc(self, bRotatings):
        self.sensor_info = bRotatings
        print("sensorinfo", self.sensor_info)
        next_states = []
        for i in range(len(self.windmills)):
            checkpins = self.windmills[i].get_read_pins(self.wind_mode)
            print("checkpins", i+1, checkpins, end="")
            states = self.get_states(checkpins)
            print("STATES", states, end="")
            next_state = self.windmills[i].next_rotating(states)
            print("nextstates", next_state)
            next_states.append(next_state)
        for i in range(len(next_states)):
            self.windmills[i].set_signal(next_states[i])

    
    def get_states(self, pins):
        l = len(pins)
        states = []
        if l is 0:
            return states
        for i in range(l):
            ind = pins[i]-1
            if ind < 30:
                s = self.windmills[ind].bRotating
            else:
                indx = ind - 30
                s = self.sensor_info[indx]
            states.append(int(s))
        return states

    def changeMode(self):
        self.wind_mode += 1
        if self.wind_mode is 3:
            self.wind_mode = 0