import time

class Timer: 
    def __init__(self):
        self.timestamp = time.time()
        self.totalTime = 0
    
    def stop(self):
        self.totalTime = time.time() - self.timestamp

    def getTotalTime(self):
        return self.totalTime
