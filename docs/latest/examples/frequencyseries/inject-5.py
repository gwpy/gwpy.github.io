from gwpy.plotter import TimeSeriesPlot
inj = injfd.ifft()
plot = TimeSeriesPlot(noise, inj, sep=True, sharex=True, sharey=True)
plot.show()