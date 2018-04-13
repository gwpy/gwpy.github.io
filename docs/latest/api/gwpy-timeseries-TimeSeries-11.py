# We can prepare one second of Gaussian noise:

from numpy import random
from gwpy.timeseries import TimeSeries
noise = TimeSeries(random.normal(scale=.1, size=16384),
                   sample_rate=16384)

# Then we can download a simulation of the GW150914 waveform from LOSC:

from astropy.utils.data import get_readable_fileobj
source = 'https://losc.ligo.org/s/events/GW150914/P150914/'
url = '%s/fig2-unfiltered-waveform-H.txt' % source
with get_readable_fileobj(url) as f:
    signal = TimeSeries.read(f, format='txt').taper()
signal.t0 = .5 # make sure this intersects with noise time samples

# Note, since this simulation cuts off before a certain time, it is
# important to taper its ends to zero to avoid ringing artifacts.
# Since the time samples overlap, we can inject this into our noise data:

data = noise.inject(signal)

# Finally, we can visualize the full process in the time domain:

from gwpy.plotter import TimeSeriesPlot
plot = TimeSeriesPlot(noise, signal, data, sep=True,
                      sharex=True, sharey=True)
plot.set_epoch(0)
plot.show()
