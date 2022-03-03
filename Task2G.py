from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.station import inconsistent_typical_range_stations
from floodysystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit
import datetime
import numpy as np

"""Task 2G: issuing flood warnings for towns"""
'''Logic used for this code:
 - checks the data for recent days and tries to assign it an equation (to have a gradient function)
 - checks the 

