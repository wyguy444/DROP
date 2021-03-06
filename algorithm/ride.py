import numpy as np

class Ride:
    def __init__(self, ride_id, name, duration, latitude, longitude, wait_time):
        self.ride_id = ride_id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.duration = duration
        self.wait_time = wait_time
    
    def __repr__(self):
        return f"{self.ride_id}. {self.name}"