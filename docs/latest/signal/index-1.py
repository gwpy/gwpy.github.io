from gwpy.timeseries import TimeSeries  # import the class
data = TimeSeries.fetch_open_data('L1', 968654500, 968654600)  # fetch data from LOSC
asd = data.asd(4, 2)  # calculated amplitude spectral density with 4-second FFT and 50% overlap
plot = asd.plot()  # make plot
ax = plot.gca()  # extract Axes
ax.set_xlabel('Frequency [Hz]')  # set X-axis label
ax.set_ylabel(r'ASD [strain/\rtHz]')  # set Y-axis label (requires latex)
ax.set_xlim(40, 2000)  # set X-axis limits
ax.set_ylim(8e-24, 5e-20)  # set Y-axis limits
ax.set_title('Strain sensitivity of LLO during S6')  # set Axes title
plot.show()  # show me the plot