# load data
from gwpy.timeseries import TimeSeries
raw = TimeSeries.fetch_open_data('L1', 1126259446, 1126259478)

# calculate filtered timeseries, and Q-transform spectrogram
data = raw.bandpass(50, 300).notch(60).crop(1126259446+1)
qtrans = raw.q_transform()

# plot
from matplotlib import pyplot
plot, axes = pyplot.subplots(nrows=2, sharex=True, figsize=(8, 6))
tax, qax = axes
tax.plot(data, color='gwpy:ligo-livingston')
qax.imshow(qtrans)
tax.set_xlabel('')
tax.set_xscale('auto-gps')
tax.set_xlim(1126259462.2, 1126259462.5)
tax.set_ylabel('Strain amplitude')
qax.set_yscale('log')
qax.set_ylabel('Frequency [Hz]')
qax.colorbar(clim=(0, 35), label='Normalised energy')