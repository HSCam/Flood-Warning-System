from sklearn.neighbors import radius_neighbors_graph
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
import numpy as np

stations = build_station_list()
def test_stations_within_radius():
    closest_station = stations_within_radius(stations, (52.2053, 0.1218), 1)
    assert closest_station == ["Cambridge Jesus Lock"]
    assert closest_station == str