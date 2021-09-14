class Fitness:
    def __init__(self, route):
        self.route = route
        self.time = 0
        self.fitness= 0.0
    
    def routeTime(self):
        if self.time == 0:
            pathTime = 0
            for i in range(0, len(self.route)):
                fromRide = self.route[i]
                toRide = None
                if i + 1 < len(self.route):
                    toRide = self.route[i + 1]
                else:
                    toRide = self.route[0]
                pathTime += fromRide.time(toRide)
            self.time = pathTime
        return self.time
    
    def routeFitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.routeTime())
        return self.fitness