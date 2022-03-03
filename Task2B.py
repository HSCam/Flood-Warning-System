from distutils.command.build import build
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    """Task 2B: Assessing flood risk by relative water level"""
    stations = build_station_list()
    update_water_levels(stations)
    stations_of_interest = stations_level_over_threshold(stations, 0.8)
    for station in stations_of_interest:
        print(station)

if __name__ == '__main__':
    print("***Task 2B: CUED Part 1A Flood Warning System***")
    run()