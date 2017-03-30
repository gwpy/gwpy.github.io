h1hoft = TimeSeries.fetch_open_data('H1', 'Sep 14 2015 09:50:29', 'Sep 14 2015 09:51:01')
ax = plot.gca()
ax.plot(h1hoft)
plot.refresh()
