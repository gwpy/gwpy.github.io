from gwpy.timeseries import TimeSeries
data = TimeSeries.fetch_open_data('L1', 1126259446, 1126259478)
plot = data.plot(figsize=(8, 4.8), ylabel='Strain',
                 color='gwpy:ligo-livingston')
plot.show()
