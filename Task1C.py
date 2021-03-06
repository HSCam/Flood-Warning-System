from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1C"""

    stations = build_station_list()
    #uses function to calculate stations within 10 of the centre given
    within_10 =  stations_within_radius(stations, (52.2053, 0.1218), 10)
    stations_within_10 = []
    #iterates through stations and appends all items to station_within_10
    for station in within_10:
        stations_within_10.append(station)
    print(sorted(stations_within_10, key=lambda x: x.name))

if __name__ == "__main__":
    print("***Task 1C: CUED Part IA FLood Warning System***")
    run()
