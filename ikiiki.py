from manager import Manager
import time

TTY = "/dev/ttyACM0"
BAUD = 115200 

class Ikiiki:
    def __init__(self):
        self.manager = Manager(TTY, BAUD)

    def main_loop(self):
        while True:
            try:
                self.manager.main()
                time.sleep(.01)
            except KeyboardInterrupt:
                break


if __name__ == '__main__':
    ikiiki = Ikiiki()
    ikiiki.main_loop()