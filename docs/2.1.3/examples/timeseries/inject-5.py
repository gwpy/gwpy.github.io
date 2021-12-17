from gwpy.plot import Plot
plot = Plot(noise, signal, data, separate=True, sharex=True, sharey=True)
plot.gca().set_epoch(0)
plot.show()