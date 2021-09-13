import numpy as np

class Ride:
    def __init__(self, x, y, duration):
        self.x = x
        self.y = y
        self.duration = duration
    
    def distance(self, ride):
        xDis = abs(self.x - ride.x)
        yDis = abs(self.y - ride.y)
        distance = np.sqrt((xDis ** 2) + (yDis ** 2))
        return distance
    
    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + "," + str(self.duration) + ")"