from gwpy.plotter import FrequencySeriesPlot
plot = FrequencySeriesPlot(numpy.abs(noisefd), numpy.abs(injfd), sep=True,
                           sharex=True, sharey=True)
plot.show()