from floodsystem.geo import river_with_stations
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1D"""
    stations = build_station_list()  # printing a list of rivers with at least one monitoring station (all contained in 'rivers' variable), followed by output of first ten alphabetically
    rivers = river_with_stations(stations)
    print("Stations:", len(rivers), "\n", "First 10 (alphabetically):", rivers[:10], "\n")

    stations_on_river = stations_by_river(stations)
    testA = stations_on_river["River Aire"]
    namesA = []
    for i in range(len(testA)):
        namesA.append(testA[i].name)
    print("Stations on the River Aire:",sorted(namesA),"\n")

    testB = stations_on_river["River Cam"]
    namesB = []
    for i in range(len(testB)):
        namesB.append(testB[i].name)
    print("Stations on the River Cam:",sorted(namesB),"\n")

    testC = stations_on_river["River Thames"]
    namesC = []
    for i in range(len(testC)):
        namesC.append(testC[i].name)
    print("Stations on the River Thames:", sorted(namesC), "\n")


if __name__ == "__main__":
    print("***Task 1D: CUED Part IA FLood Warning System")
    run()