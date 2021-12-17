from numpy import random
from gwpy.timeseries import TimeSeries
noise = TimeSeries(random.normal(scale=.1, size=1024), sample_rate=1024)