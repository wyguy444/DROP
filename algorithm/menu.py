import csv
import os
import sys
from genetic_algorithm import GeneticAlgorithm
from ride import Ride


ride_dict = {}

with open(os.path.join(os.path.dirname(sys.argv[0]), '../data/rides.csv')) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            ride_dict[int(row[0])] = Ride(
                int(row[0]),
                row[1],
                float(row[2]),
                float(row[4]),
                float(row[5]),
                int(row[6])
            )

travel_times = []

with open(os.path.join(os.path.dirname(sys.argv[0]), '../data/travel_times.csv')) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
       travel_times.append([float(time) for time in row])

ride_choices = {}
print("Ride Options:\n")
for key, value in ride_dict.items():
        if key != 0:
            print(value)
print("================================================================\n")
while True:
    print("Current ride choices")
    for key, value in ride_choices.items():
            print(value)
    print("================================================================\n")
    ride = input("Enter number, re-type ride number to remove it from the list. (list) for list of rides, (clear) to clear, (done) when finished\n")
    if ride == "list":
        for key, value in ride_dict.items():
            if key != 0:
                print(value)
        print("================================================================\n")
        continue
    elif ride == "clear":
        ride_choices = {}
        continue
    elif ride == "done":
        break
    elif not ride.isnumeric():
        print("Please enter a valid ride number, or one of the command options.\n")
        continue
    ride = int(ride)
    if ride in ride_choices.keys():
        ride_choices.pop(ride)
        continue
    elif ride in ride_dict.keys():
        ride_choices[ride] = ride_dict[ride]
        continue
    else:
        print("Ride not found, check the options for a list of rides\n")
        continue

algorithm = GeneticAlgorithm(ride_dict, travel_times)
route, details = algorithm.determine_optimal_route(ride_choices)
total_time = details[0]
time_list = details[1]

with open(os.path.join(os.path.dirname(sys.argv[0]), '../data/output.csv'), 'w', newline='') as csv_file:
    csvwriter = csv.writer(csv_file)
    csvwriter.writerow(['id', 'name', 'travel_time', 'wait_time', 'duration', 'latitude', 'longitude'])
    csvwriter.writerow([0, 'Entrance', 0, 0, 0, 33.809479, -117.918985])
    total_time = 0
    for ride_id in route:
        step_time = time_list[route.index(ride_id)]
        total_time += step_time
        ride = ride_dict[ride_id]
        csvwriter.writerow([
            ride_id,
            ride.name,
            step_time,
            ride.wait_time,
            ride.duration,
            ride.latitude,
            ride.longitude
        ])
    step_time = time_list[-1]
    total_time += step_time
    csvwriter.writerow([0, 'Entrance', step_time, 0, 0, 33.809479, -117.918985])