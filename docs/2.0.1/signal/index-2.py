# To create a low-pass filter at 1000 Hz for 4096 Hz-sampled data:

from gwpy.signal.filter_design import lowpass
lp = lowpass(1000, 4096)

# To view the filter, you can use the `~gwpy.plot.BodePlot`:

from gwpy.plot import BodePlot
plot = BodePlot(lp, sample_rate=4096)
plot.show()
