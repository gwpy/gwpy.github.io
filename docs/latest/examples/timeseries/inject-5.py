from gwpy.plotter import TimeSeriesPlot
plot = TimeSeriesPlot(noise, signal, data, sep=True, sharex=True, sharey=True)
plot.set_epoch(0)
plot.show()