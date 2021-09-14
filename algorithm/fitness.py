class Fitness:
    def __init__(self, ride_dict, travel_times):
        self.ride_dict = ride_dict
        self.travel_times = travel_times

    def determine_fitness(self, route):
        time = self.travel_times[0][route[0]]
        for ride_id in route:
            time += self.ride_dict[ride_id].wait_time
            time += self.ride_dict[ride_id].duration
            if route.index(ride_id) < (len(route) - 1):
                time += self.travel_times[ride_id][route[route.index(ride_id) + 1]]
        time += self.travel_times[route[-1]][0]
        return time

    def get_full_route_stats(self, route):
        travel_time_list = []
        time = self.travel_times[0][route[0]]
        travel_time_list.append(time)
        for ride_id in route:
            time += self.ride_dict[ride_id].wait_time
            time += self.ride_dict[ride_id].duration
            if route.index(ride_id) < (len(route) - 1):
                tt = self.travel_times[ride_id][route[route.index(ride_id) + 1]]
                travel_time_list.append(tt)
                time += tt
        tt = self.travel_times[route[-1]][0]
        travel_time_list.append(tt)
        time += tt
        return (round(time, 2), travel_time_list)
