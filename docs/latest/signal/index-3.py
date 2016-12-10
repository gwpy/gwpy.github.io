from gwpy.plotter import TimeSeriesPlot
bp = data.filter(f).crop(1126259446+2, 1126259446-2)
plot = TimeSeriesPlot(data.crop(1126259446+2, 1126259446-2), bp, sep=True)
plot.show()