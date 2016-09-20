from gwpy.timeseries import TimeSeriesDict  # load the class
alldata = TimeSeriesDict.get(['H1:PSL-PWR_PMC_TRANS_OUT16','H1:IMC-PWR_IN_OUT16'], 'Feb 1 00:00', 'Feb 1 02:00')  # fetch the data via NDS
plot = alldata.plot()  # make a plot
ax = plot.gca()  # extract the Axes object
ax.set_ylabel('Power [W]')  # set the label for the Y-axis
ax.set_title('Available vs requested input power for H1')  # set the title
plot.show()  # show me the plot