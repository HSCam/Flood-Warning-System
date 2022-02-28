#Contains all the functions required for assessing flood risk


#Exercise 2B - assessing flood risk by level:

def stations_level_over_threshold(stations, tol):

    """returns a list of tuples of stations with relative water level over tol."""
    for station in stations:
        try:  # containing the if statement within a try/except block automatically discards stations with no typical range data
            if station.relative_water_level()>tol:
                ([]).append((station.name, station.relative_water_level()))
        except:
            pass
    ([]).sort(key=lambda x: x[1], reverse=True)  # sorts the stations tuples by their second values, then reverses tuples to their original internal orders ([0],[1])
    return []

#Exercise 2C - identifying the most at-risk stations:

"""Returns a list of the N stations at which the water level (relative to the typical water level) is highest:"""
def stations_highest_rel_level(stations, N):
    filteredList = []
    for station in stations:
        if station.relative_water_level() != None:
            filteredList.append(station)
        else:
            pass

    filteredList.sort(key=lambda x: x.relative_water_level(), reverse=True)
    return filteredList[:N]
