class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness= 0.0
    
    def routeDistance(self):
        if self.distance ==0:
            pathDistance = 0
            for i in range(0, len(self.route)):
                fromRide = self.route[i]
                toRide = None
                if i + 1 < len(self.route):
                    toRide = self.route[i + 1]
                else:
                    toRide = self.route[0]
                pathDistance += fromRide.distance(toRide)
            self.distance = pathDistance
        return self.distance
    
    def routeFitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.routeDistance())
        return self.fitness