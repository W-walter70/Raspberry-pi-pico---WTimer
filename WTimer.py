# WTimer class is written by Ing. Walter Porcellini , Milan (Italy)

class WTon:
    Preset = 0
    Counter = 0
    Done = False

    def __init__(self, preset):
        self.Preset = preset
        self.Counter = 0
        self.Done = False

    def run(self, delta_time, start):
        if start and self.Counter < self.Preset:
            self.Counter += delta_time

        if not start:
            self.Counter = 0

        self.Done = start and (self.Counter >= self.Preset)

    def getOutput(self):
        return self.Done


class WTof:
    Preset = 0
    Counter = 0
    Done = False
    Memory = False

    def __init__(self, preset):
        self.Preset = preset
        self.Counter = 0
        self.Done = False
        self.Memory = False

    def run(self, delta_time, start):
        if start:
            self.Memory = True

        if not start and self.Memory and self.Counter < self.Preset:
            self.Counter += delta_time

        if self.Counter >= self.Preset:
            self.Memory = False
            self.Counter = 0

        self.Done = start or (self.Counter < self.Preset and self.Memory == True)

    def getOutput(self):
        return self.Done





