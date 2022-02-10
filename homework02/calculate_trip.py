import json
import math

def calculate_travel_time(sites_data) -> float:
    starting_latitude = 16
    starting_longitude = 82

    total_distance = 0

    for i in range(5):
        if (i == 0):
            total_distance += calc_gcd(16, 82, sites_data['sites'][i]['latitude'], sites_data['sites'][i]['longitude'])
        else:
            total_distance += calc_gcd(sites_data['sites'][i - 1]['latitude'], sites_data['sites'][i - 1]['longitude'], sites_data['sites'][i]['latitude'], sites_data['sites'][i]['longitude'])

    return (total_distance/10)

def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    mars_radius = 3389.5
    lat1, lon1, lat2, lon2 = map(math.radians, [latitude_1, longitude_1, latitude_2, longitude_2])
    d_sigma = math.acos(math.sin(lat1)*math.sin(lat2) + math.cos(lat1)*math.cos(lat2)*math.cos(abs(lon1-lon2)))
    return (mars_radius*d_sigma)

def calculate_sample_time(sites_data) -> float:
    sample_time = 0
    for i in range(5):
        if (sites_data['sites'][i]['composition'] == 'stony'):
            sample_time += 1
        if (sites_data['sites'][i]['composition'] == 'iron'):
            sample_time += 2
        else:
            sample_time += 3

    return sample_time

def main():
    with open("sites.json", "r") as f:
        sites_data = json.load(f)

    travel_time = calculate_travel_time(sites_data)
    sample_time = calculate_sample_time(sites_data)
    total_time = travel_time + sample_time

    print('total travel time = ' + str(travel_time) + ' hr, total sample time = ' + str(sample_time) + ' hr, total time = ' + str(total_time) + ' hr')

if __name__ == '__main__':
    main()
