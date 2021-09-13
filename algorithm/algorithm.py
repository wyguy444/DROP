import csv
import os
import sys


ride_list = []

with open(os.path.join(os.path.dirname(sys.argv[0]), 'rides.csv')) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            ride_list.append(row[1].lower())
            print(f'Ride Name: {row[1]}, duration: {row[2]} min')

ride_choices = []
while True:
    print("Current ride choices")
    print("\n".join(ride_choices))
    print("================================================================")
    ride = input("Enter ride name, re-type name to remove it from the list. (1) for list of rides, (2) to clear, (3) when finished\n")
    ride = ride.upper()
    if ride == "1":
        print("\n".join(ride_list))
        continue
    elif ride == "2":
        ride_choices = []
        continue
    elif ride == "3":
        break
    elif ride in ride_choices:
        ride_choices.remove(ride)
        continue
    elif ride.lower() in ride_list:
        ride_choices.append(ride)
        continue
    else:
        print("Ride not found, check your spelling")
        continue



