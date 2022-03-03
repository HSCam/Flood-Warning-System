"""Testing program for Task 2B"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold


def test1_stations_over_threshold():
    """testing appropriate stations are excluded"""
    stations = build_station_list()
    stations = stations[:20]
    stations1 = stations_level_over_threshold(stations, 2000)
    assert len(stations1) == 0
