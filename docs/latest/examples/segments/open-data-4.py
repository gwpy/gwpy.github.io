l1month1 = DataQualityFlag.fetch_open_data('L1_DATA', 'Sep 12 2015',
                                           'Oct 12 2015')
bothon = h1month1 & l1month1
plot = h1month1.plot()
ax = plot.gca()
ax.plot(l1month1)
ax.plot(bothon, label='Both')
plot.show()