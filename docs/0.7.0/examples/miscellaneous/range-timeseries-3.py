import numpy
from gwpy.astro import inspiral_range
h1range = TimeSeries(numpy.zeros(len(h1spec)),
                     dt=h1spec.dt, t0=h1spec.t0, unit='Mpc')
l1range = h1range.copy()
for i in range(h1range.size):
    h1range[i] = inspiral_range(h1spec[i], fmin=10)
    l1range[i] = inspiral_range(l1spec[i], fmin=10)