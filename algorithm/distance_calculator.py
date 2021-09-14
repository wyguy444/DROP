import csv
import os
import sys
import geopy.distance


ride_coordinates = {}

with open(os.path.join(os.path.dirname(sys.argv[0]), '../data/rides.csv')) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            ride_coordinates[row[0]] = (row[4], row[5])

rows = []

for from_ride in ride_coordinates:
    row = []
    for to_ride in ride_coordinates:
        distance = geopy.distance.distance(ride_coordinates[from_ride], ride_coordinates[to_ride]).km
        time = distance*20
        row.append(round(time, 2))
    rows.append(row)

with open(os.path.join(os.path.dirname(sys.argv[0]), '../data/travel_times.csv'), 'w') as csv_file:
    csvwriter = csv.writer(csv_file)
    csvwriter.writerows(rows)