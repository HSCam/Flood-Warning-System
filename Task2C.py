from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import *

def run():
    """Task 2C: identifying the most at-risk stations"""
    stations = build_station_list()
    update_water_levels(stations)
    atRiskStations = stations_highest_rel_level(stations, 10)
    for station in atRiskStations:
        print(station.name, station.relative_water_level())

if __name__ == "__main__":
    print("*** Task 2C: CUED Part 1A Flood Warning System***")
    run()