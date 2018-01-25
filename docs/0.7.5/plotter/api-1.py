import numpy
from gwpy.plotter import Plot

# To plot a simple image and add a colorbar:

plot = Plot()
ax = plot.gca()
ax.imshow(numpy.random.randn(120).reshape((10, 12)))
plot.add_colorbar(label='Value')
plot.show()
