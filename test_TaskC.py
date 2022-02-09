from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius


stations = build_station_list()
def test_stations_within_radius():
    closest_station = stations_within_radius(stations, (52.2053, 0.1218), 10)
    assert closest_station[0].name == "Cambridge Jesus Lock"
 