# To create a low-pass filter at 1000 Hz for 4096 Hz-sampled data:

from gwpy.signal.filter_design import notch
n = notch(100, 4096)

# To view the filter, you can use the `~gwpy.plotter.BodePlot`:

from gwpy.plotter import BodePlot
plot = BodePlot(n, sample_rate=4096)
plot.show()
