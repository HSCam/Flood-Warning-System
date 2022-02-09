from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation

def test_stations_by_distance():
    stations = build_station_list()
    #Runs the function with 
    distance = stations_by_distance(stations, (52.2053, 0.1218))
    #Checks all the types are correct
    assert type(distance) == list
    assert type(distance[0][0]) == MonitoringStation
    assert type(distance[0][1]) == float
    #Checks that the list is in the right order
    for i in range(10):
        assert distance[i][1] < distance[i+1][1]

