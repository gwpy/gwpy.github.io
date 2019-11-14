from gwpy.plot import Plot
plot = Plot(data, white, separate=True, sharex=True)
plot.axes[0].set_ylabel('Y-arm power [counts]', fontsize=16)
plot.axes[1].set_ylabel('Whitened amplitude', fontsize=16)
plot.show()