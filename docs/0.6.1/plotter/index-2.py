data2 = TimeSeries.fetch('L1:LDAS-STRAIN', 968654552, 968654562)
from gwpy.plotter import TimeSeriesPlot
plot2 = TimeSeriesPlot()
ax2 = plot2.gca()
ax2.plot(data, color='k', linestyle='--')
ax2.plot(data2, color='r', linestyle=':')
plot2.show()
