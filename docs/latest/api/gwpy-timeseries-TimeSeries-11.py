# To see the effect of the Planck-taper window, we can taper a
# sinusoidal `TimeSeries` at both ends:

import numpy
from gwpy.timeseries import TimeSeries
t = numpy.linspace(0, 1, 2048)
series = TimeSeries(numpy.cos(10.5*numpy.pi*t), times=t)
tapered = series.taper()

# We can plot it to see how the ends now vary smoothly from 0 to 1:

from gwpy.plotter import TimeSeriesPlot
plot = TimeSeriesPlot(series, tapered, sep=True, sharex=True)
plot.show()
