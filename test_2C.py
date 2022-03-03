from floodsystem.flood import *
from floodsystem.stationdata import build_station_list, update_water_levels

def test1_Task2C():
    stations = build_station_list()
    update_water_levels(stations)
    stations = stations[:10]
    atrisk = stations_highest_rel_level(stations)
    for station in atrisk:
        typecheck = type(station.relative_water_level())
        if typecheck == NoneType:
            raise TypeError()
        else:
            assert len(atrisk) == 10