from gwpy.timeseries import TimeSeries
hdata = TimeSeries.fetch_open_data('H1', 1126259446, 1126259478)
ldata = TimeSeries.fetch_open_data('L1', 1126259446, 1126259478)
from gwpy.plot import Plot
plot = Plot(hdata, ldata, figsize=(12, 4))
plot.show()
