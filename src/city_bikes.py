# Write your solution here
from math import sqrt

def get_station_data(filename: str):
    station_locations = {}
    file_format = []
    with open(filename) as s_file:
        for line in s_file:
            line = line.strip()
            parts = line.split(";")

            if 'id' in parts:
                file_format = parts[:]
                continue

            name = file_format.index("name")
            longitude =  file_format.index("Longitude")
            latitude = file_format.index("Latitude")

            station_locations[parts[name]] = (float(parts[longitude]), float(parts[latitude]))
            """
               Remember:
               longitude located in index 0 in tuple
               latitud located in index 1 in tuple
            """
    
    return station_locations

def distance(stations: dict, station1: str, station2: str):
    s1_long_lat = stations[station1]
    s2_long_lat = stations[station2]
    
    long1 = s1_long_lat[0]
    long2 = s2_long_lat[0]
    lat1 = s1_long_lat[1]
    lat2 = s2_long_lat[1]

    x = (long1 - long2) * 55.26
    y = (lat1 - lat2) * 111.2

    return sqrt(x**2 + y**2)

def greatest_distance(stations: dict):
    
    longest = ()
    most = 0
    for key in stations:
        for k in stations:

            if key == k:
                continue

            d = distance(stations, key, k)

            if d >= most:
                longest = (key, k, d)
                most = d

    return longest


if __name__ == "__main__":
    stations = get_station_data("stations1.csv")
    gd = greatest_distance(stations)
    for i in gd:
        print(f"{i} ", end="")
    
    