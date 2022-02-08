from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


stations = build_station_list()
within_10 =  stations_within_radius(stations, (52.2053, 0.1218), 10)
stations_within_10 = []
for station in within_10:
    stations_within_10.append(station)
print(sorted(stations_within_10))