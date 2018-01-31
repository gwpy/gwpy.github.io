from numpy.random import normal
from scipy.signal import gausspulse
from gwpy.timeseries import TimeSeries

# Generate a `TimeSeries` containing Gaussian noise sampled at 4096 Hz,
# centred on GPS time 0, with a sine-Gaussian pulse ('glitch') at
# 500 Hz:

noise = TimeSeries(normal(loc=1, size=4096*4), sample_rate=4096, epoch=-2)
glitch = TimeSeries(gausspulse(noise.times.value, fc=500) * 4, sample_rate=4096)
data = noise + glitch

# Compute and plot the Q-transform of these data:

q = data.q_transform()
plot = q.plot()
plot.set_xlim(-.2, .2)
plot.set_epoch(0)
plot.show()
