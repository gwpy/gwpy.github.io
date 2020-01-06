from __future__ import division
import numpy
from matplotlib import (pyplot, rcParams)
from matplotlib.colors import to_hex
from gwpy.plot import colors

rcParams.update({
    'text.usetex': False,
    'font.size': 15
})

th = numpy.linspace(0, 2*numpy.pi, 512)
names = [
     'gwpy:geo600',
     'gwpy:kagra',
     'gwpy:ligo-hanford',
     'gwpy:ligo-india',
     'gwpy:ligo-livingston',
     'gwpy:virgo',
]

fig = pyplot.figure(figsize=(5, 2))
ax = fig.gca()
ax.axis('off')

for j, name in enumerate(sorted(names)):
    c = str(to_hex(name))
    v_offset = -(j / len(names))
    ax.plot(th, .1*numpy.sin(th) + v_offset, color=c)
    ax.annotate("{!r}".format(name), (0, v_offset), xytext=(-1.5, 0),
                ha='right', va='center', color=c,
                textcoords='offset points', family='monospace')
    ax.annotate("{!r}".format(c), (2*numpy.pi, v_offset), xytext=(1.5, 0),
                ha='left', va='center', color=c,
                textcoords='offset points', family='monospace')

fig.subplots_adjust(**{'bottom': 0.0, 'left': 0.54,
                       'right': 0.78, 'top': 1})
pyplot.show()