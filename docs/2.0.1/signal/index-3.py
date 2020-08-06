# To create a high-pass filter at 100 Hz for 4096 Hz-sampled data:

from gwpy.signal.filter_design import highpass
hp = highpass(100, 4096)

# To view the filter, you can use the `~gwpy.plot.BodePlot`:

from gwpy.plot import BodePlot
plot = BodePlot(hp, sample_rate=4096)
plot.show()
