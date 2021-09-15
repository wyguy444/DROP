import copy

class Fitness:
    def __init__(self, ride_dict, travel_times):
        self.ride_multipliers = {
            0: .5,
            1: .75,
            2: 1,
            3: 1,
            4: 1.25,
            5: 1.25,
            6: 1.25,
            7: 1,
            8: 1,
            9: 1,
            10: 1,
            11: 1,
            12: .75,
            13: .75,
            14: .5,
        }
        self.ride_dict = ride_dict
        self.travel_times = travel_times

    def determine_fitness(self, route):
        time = self.travel_times[0][route[0]]
        step = 0
        for ride_id in route:
            hours = int(time/60)
            time += self.ride_dict[ride_id].wait_time * self.ride_multipliers[hours % 14]
            time += self.ride_dict[ride_id].duration
            if step < (len(route) - 1):
                time += self.travel_times[ride_id][route[step + 1]]
            step += 1
        time += self.travel_times[route[-1]][0]
        return time

    def get_full_route_stats(self, route):
        travel_time_list = []
        route_ride_list = []
        time = self.travel_times[0][route[0]]
        travel_time_list.append(time)
        step = 0
        for ride_id in route:
            hours = int(time/60)
            ride_wait = self.ride_dict[ride_id].wait_time * self.ride_multipliers[hours % 14]
            route_ride_list.append(copy.deepcopy(self.ride_dict[ride_id]))
            route_ride_list[-1].wait_time = ride_wait
            time += ride_wait
            time += self.ride_dict[ride_id].duration
            if step < (len(route) - 2):
                tt = self.travel_times[ride_id][route[step + 1]]
                travel_time_list.append(tt)
                time += tt
            step += 1
        tt = self.travel_times[route[-1]][0]
        travel_time_list.append(tt)
        time += tt
        return (round(time, 2), travel_time_list, route_ride_list)
