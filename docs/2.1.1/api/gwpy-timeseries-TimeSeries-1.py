from gwpy.timeseries import TimeSeries

# To create an array of random numbers, sampled at 100 Hz, in units of
# 'metres':

from numpy import random
series = TimeSeries(random.random(1000), sample_rate=100, unit='m')

# which can then be simply visualised via

plot = series.plot()
plot.show()
