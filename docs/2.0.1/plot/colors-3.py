from matplotlib import pyplot
from gwpy.plot.colors import GW_OBSERVATORY_COLORS
fig = pyplot.figure()
ax = fig.gca()
ax.plot([1, 2, 3, 4, 5], color=GW_OBSERVATORY_COLORS['L1'])
fig.show()