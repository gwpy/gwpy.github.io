from gwpy.timeseries import TimeSeries
data = TimeSeries.fetch('H1:LDAS-STRAIN', 968654552, 968654562)
plot = data.plot()
plot.show()
