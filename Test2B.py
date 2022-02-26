"""Testing program for Task 2B"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def test1_stations_over_threshold():
    """testing for sensible relative water levels"""
    stations = build_station_list()
    update_water_levels(stations)
    stations = stations[:100]
    for station in stations:
        assert station.relative_water_level()<100 and station.relative_water_level()>-100

def test2_stations_over_threshold():
    """testing appropriate stations are excluded"""
    stations = stations[:20]
    stations1 = stations_level_over_threshold(stations, -2000)
    assert len(stations1) == len(stations)
    stations2 = stations_level_over_threshold(stations, 2000)
    assert len(stations2) == 0
