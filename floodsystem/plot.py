import matplotlib
import matplotlib.pyplot as plt


def plot_water_levels(station, dates, levels):

    plt.plot(dates, levels)
    typical_high = station.typical_range[1]
    typical_low = station.typical_range[0]
    high = []
    low = []
    length_dates = len(dates)
    for i in range (length_dates):
        high.append(typical_high)
        low.append(typical_low)
    plt.plot(dates, high)
    plt.plot(dates, low)
    plt.xlabel("date")
    plt.ylabel("water level (m)")
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.tight_layout()
    plt.show()