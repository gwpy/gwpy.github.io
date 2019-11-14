# We can design an arbitrarily complicated filter using
# :mod:`gwpy.signal.filter_design`

from gwpy.signal import filter_design
bp = filter_design.bandpass(50, 250, 4096.)
notches = [filter_design.notch(f, 4096.) for f in (60, 120, 180)]
zpk = filter_design.concatenate_zpks(bp, *notches)

# And then can download some data from LOSC to apply it using
# `TimeSeries.filter`:

from gwpy.timeseries import TimeSeries
data = TimeSeries.fetch_open_data('H1', 1126259446, 1126259478)
filtered = data.filter(zpk, filtfilt=True)

# We can plot the original signal, and the filtered version, cutting
# off either end of the filtered data to remove filter-edge artefacts

from gwpy.plot import Plot
plot = Plot(data, filtered[128:-128], separate=True)
plot.show()
