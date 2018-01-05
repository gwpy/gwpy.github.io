from gwpy.timeseries import TimeSeries
h1 = TimeSeries.fetch_open_data('H1', 1126259457, 1126259467)
plot = h1.plot()
plot.show()
