# Demodulation is useful when trying to examine steady sinusoidal
# signals we know to be contained within data. For instance,
# we can download some data from LOSC to look at trends of the
# amplitude and phase of Livingston's calibration line at 331.3 Hz:

from gwpy.timeseries import TimeSeries
data = TimeSeries.fetch_open_data('L1', 1131350417, 1131357617)

# We can demodulate the `TimeSeries` at 331.3 Hz with a stride of once
# per minute:

amp, phase = data.demodulate(331.3, stride=60)

# We can then plot these trends to visualize changes in the amplitude
# and phase of the calibration line:

from gwpy.plotter import TimeSeriesPlot
plot = TimeSeriesPlot(amp, phase, sep=True, sharex=True)
plot.show()
