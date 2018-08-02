# To create a band-pass filter for 100-1000 Hz for 4096 Hz-sampled data:

from gwpy.signal.filter_design import bandpass
bp = bandpass(100, 1000, 4096)

# To view the filter, you can use the `~gwpy.plot.BodePlot`:

from gwpy.plot import BodePlot
plot = BodePlot(bp, sample_rate=4096)
plot.show()
