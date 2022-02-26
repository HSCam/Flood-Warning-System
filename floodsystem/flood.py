#Contains all the functions required for assessing flood risk


#Exercise 2B:

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

