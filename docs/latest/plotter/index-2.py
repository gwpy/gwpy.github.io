l1 = TimeSeries.fetch_open_data('L1', 1126259457, 1126259467)
from gwpy.plotter import TimeSeriesPlot
plot = TimeSeriesPlot()
ax = plot.gca()
ax.plot(h1, color='gwpy:ligo-hanford')
ax.plot(l1, color='gwpy:ligo-livingston')
ax.set_ylabel('Strain noise')
plot.show()
