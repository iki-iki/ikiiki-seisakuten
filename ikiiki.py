from manager import Manager

TTY = "/dev/ttyACM0"
BAUD = 115200 

class Ikiiki:
    def __init__(self):
        self.manager = Manager(TTY, BAUD)

    def main_loop(self):
        self.manager.thread_init()
        self.manager.main()


ikiiki = Ikiiki()
ikiiki.main_loop()