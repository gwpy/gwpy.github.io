from gwpy.timeseries import TimeSeries
raw = TimeSeries.fetch_open_data('L1', 1126259446, 1126259478)
data = raw.bandpass(50, 300).notch(60).crop(*raw.span.contract(1))
plot = data.plot(xscale='auto-gps')
plot.show()
