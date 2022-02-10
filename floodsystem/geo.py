# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key
from operator import itemgetter 
#Exercise 1
''' creates a set containing the names of all the rivers with stations'''
def river_with_stations(stations):
    station_rivers = set([])  #using a 'set' object for this function as it only allows unique entries. This means the data doesn't need to be manually filtered to prevent duplicates.
    for stat in stations:
        station_rivers.add(stat.river)
    return sorted(station_rivers)  # returns a sorted list of the stations

'''creates a dictionary which maps the rivers with the names of the stations on them'''
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


#Exercise 1E:
'''returns the top N rivers by descending number of stations (including all rivers with the same number of stations, so may return more than N river names)'''
def rivers_by_station_number(stations, N):
    rivers_dict = stations_by_river(stations)  # creates a dictionary of rivers with stations
    rivers_list = map(list, rivers_dict.items())  # creates a list of the dictionary's key-item pairs as paired terms
    rivers_with_station_number = []
    for i in rivers_list:
        station_num = len(i[1])  # checks the number of stations for river 'i'
        to_append = (i[0], station_num)
        rivers_with_station_number.append(to_append)        
    rivers_with_station_number.sort(key=lambda x: x[1], reverse=True)  # sorts tuples in list by second value (number of stations), then flips within tuples to have river name first
    #print(rivers_with_station_number)
    output_list = rivers_with_station_number[:N]  # Outputs the first N terms in the sorted list
    #print(output_list)
    for check in rivers_with_station_number:  # adds on rivers which have the same number of stations as the Nth river
        number_of_stations = list(map(itemgetter(1), output_list))  # creates a list of the number of stations (excluded river names) in order
        if check[1] == number_of_stations[-1]:
            output_list.append(check)
    return(output_list)
