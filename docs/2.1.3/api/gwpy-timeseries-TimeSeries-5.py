# Heterodyning can be useful in analysing quasi-monochromatic signals
# with a known phase evolution, such as continuous-wave signals
# from rapidly rotating neutron stars. These sources radiate at a
# frequency that slowly decreases over time, and is Doppler modulated
# due to the Earth's rotational and orbital motion.

# To see an example of heterodyning in action, we can simulate a signal
# whose phase evolution is described by the frequency and its first
# derivative with respect to time. We can download some O1 era
# LIGO-Livingston data from GWOSC, inject the simulated signal, and
# recover its amplitude.

from gwpy.timeseries import TimeSeries
data = TimeSeries.fetch_open_data('L1', 1131350417, 1131354017)

# We now need to set the signal parameters, generate the expected
# phase evolution, and create the signal:

import numpy
f0 = 123.456789  # signal frequency (Hz)
fdot = -9.87654321e-7  # signal frequency derivative (Hz/s)
fepoch = 1131350417  # phase epoch
amp = 1.5e-22  # signal amplitude
phase0 = 0.4  # signal phase at the phase epoch
times = data.times.value - fepoch
phase = 2 * numpy.pi * (f0 * times + 0.5 * fdot * times**2)
signal = TimeSeries(amp * numpy.cos(phase + phase0),
                    sample_rate=data.sample_rate, t0=data.t0)
data = data.inject(signal)

# To recover the signal, we can bandpass the injected data around the
# signal frequency, then heterodyne using our phase model with a stride
# of 60 seconds:

filtdata = data.bandpass(f0 - 0.5, f0 + 0.5)
het = filtdata.heterodyne(phase, stride=60, singlesided=True)

# We can then plot signal amplitude over time (cropping the first two
# minutes to remove the filter response):

plot = het.crop(het.x0.value + 180).abs().plot()
ax = plot.gca()
ax.set_ylabel("Strain amplitude")
plot.show()
