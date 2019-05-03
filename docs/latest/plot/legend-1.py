import gwpy  # <- import anything from gwpy
from matplotlib import pyplot
fig = pyplot.figure()
ax = fig.gca()
ax.plot(range(10), label='My data')
ax.legend()
fig.show()
