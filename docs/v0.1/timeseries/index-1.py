from gwpy.timeseries import TimeSeries  # load the class
gwdata = TimeSeries.fetch_open_data('H1', 968654552, 968654562)  # fetch data from LOSC
plot = gwdata.plot()  # make a plot
ax = plot.gca()  # extract the Axes object
ax.set_ylabel('Gravitational-wave amplitude [strain]')  # set the label for the Y-axis
ax.set_title('LIGO Hanford Observatory data')  # set the title
plot.show()  # show me the plot