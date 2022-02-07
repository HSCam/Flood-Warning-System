# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

#Exercise 1D
def river_with_stations(stations):
    station_rivers = set([])  #using a 'set' object for this function as it only allows unique entries. This means the data doesn't need to be manually filtered to prevent duplicates.
    for stat in stations:
        station_rivers.add(stat.river)
    return sorted(station_rivers)  # returns a sorted list of the stations


def stations_by_river(stations):  # Maps river names to stations
    stations_on_river = {}
    rivers = river_with_stations(stations)
    for i in rivers:  # for loop through the list of rivers with stations
        stats_on_river = []  # creates a blank dictionary to link the rivers with their stations
        for x in stations:
            if x.river == i:
                stats_on_river.append(x)
        stations_on_river[i] = list(stats_on_river) # adds lists to the dictionary
    return stations_on_river

