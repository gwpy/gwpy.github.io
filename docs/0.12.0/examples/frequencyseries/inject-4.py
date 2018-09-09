from gwpy.plot import Plot
plot = Plot(numpy.abs(noisefd), numpy.abs(injfd), separate=True,
            sharex=True, sharey=True, xscale='log', yscale='log')
plot.show()