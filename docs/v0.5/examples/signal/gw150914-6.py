from gwpy.plotter import TimeSeriesPlot
plot = TimeSeriesPlot(
    data.crop(*data.span.contract(1)),
    b.crop(*b.span.contract(1)),
    figsize=[12, 8], sep=True, sharex=True)
plot.axes[0].set_title('LIGO-Hanford strain data around GW150914')
plot.axes[0].text(
    1.0, 1.0, 'Unfiltered data',
    transform=plot.axes[0].transAxes, ha='right')
plot.axes[0].set_ylabel('Amplitude [strain]', y=-0.2)
plot.axes[1].text(
    1.0, 1.0, '50-250\,Hz bandpass, notches at 60, 120, 180 Hz',
    transform=plot.axes[1].transAxes, ha='right')
plot.show()