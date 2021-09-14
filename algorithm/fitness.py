def determine_fitness(route, ride_dict, travel_time):
    time = travel_time[0][route[0]]
    for ride_id in route:
        time += ride_dict[ride_id].wait_time
        time += ride_dict[ride_id].duration
        if route.index(ride_id) < (len(route) - 1):
            time += travel_time[ride_id][route[route.index(ride_id) + 1]]
    time += travel_time[route[-1]][0]
    return time