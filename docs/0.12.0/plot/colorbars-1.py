import numpy
data = numpy.random.rand(100, 100)
from gwpy.timeseries import TimeSeries
from matplotlib import pyplot
fig, axes = pyplot.subplots(nrows=3, figsize=(6.4, 8))
for ax in axes:  # plot the same data on each
   ax.imshow(data)
fig.colorbar(axes[1].images[0], ax=axes[1])  # matplotlib default
axes[2].colorbar()  # gwpy colorbar
pyplot.show()