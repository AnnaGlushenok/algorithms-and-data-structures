import time


class Object:
    def __init__(self, int, string, time):
        self.int = int
        self.string = string
        self.time = time

    def to_string(self):
        s = "{} {} {}".format(self.int, self.string, self.time)
        return s
