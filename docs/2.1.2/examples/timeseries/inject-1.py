from numpy import random
from gwpy.timeseries import TimeSeries
noise = TimeSeries(random.normal(scale=.1, size=16384), sample_rate=16384)