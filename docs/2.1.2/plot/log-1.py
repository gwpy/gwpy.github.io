import gwpy  # <-- import anything from gwpy to active custom formatter
import numpy
from matplotlib import pyplot
fig = pyplot.figure()
ax = fig.gca()
ax.plot(numpy.arange(.1, 5, step=.1))
ax.set_xscale('log')
ax.set_yscale('log')
fig.show()
