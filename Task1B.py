def run():
    from floodsystem.stationdata import build_station_list
    from floodsystem.geo import stations_by_distance

    stations = build_station_list()
    station_distances =  stations_by_distance(stations, (52.2053, 0.1218))
    stations2 = []
    for station in station_distances:
        stations2.append((station[0].name, station[0].town,station[1]))

    closest = stations2[:10]
    furthest = stations2[-10:]

    print("The 10 closest stations are:", closest)
    print("The 10 furthest stations are:", furthest)
if __name__ == "__main__":
    run()