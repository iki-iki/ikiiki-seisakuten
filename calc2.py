from collections import deque
from wind import Wind

class Wind_Operator:
    def __init__(self):
        self.winds = deque()
        self.wind_mode = 0

    def changeMode(self):
        self.wind_mode += 1
        if self.wind_mode is 3:
            self.wind_mode = 0

    def add_wind(self, sensor_index, mode):
        w = Wind(mode, sensor_index)
        self.winds.append(w)

    def handle_new_winds(self, winds):
        for i, w in enumerate(winds):
            if w is True:
                self.add_wind(i, self.wind_mode)

    def get_winds_place(self):
        tmp_queue = deque()
        winds_places = [0] * 30 
        wi = 0
        while len(self.winds) is not 0:
            wi += 1
            w = self.winds.popleft()
            positions = w.get_next()
            # print("positions", wi, positions)
            if len(positions) is not 0:
                for i in range(len(positions)):
                    ind = positions[i] - 1
                    winds_places[ind] = 1
            if w.is_alive():
                tmp_queue.append(w)
        
        while len(tmp_queue) is not 0:
            tw = tmp_queue.popleft()
            self.winds.append(tw)

        return winds_places

