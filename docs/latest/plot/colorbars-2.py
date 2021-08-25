from gwpy.timeseries import TimeSeries
data = TimeSeries.fetch_open_data('L1', 1187008866, 1187008898)
specgram = data.spectrogram2(fftlength=.5, overlap=.25,
                             window='hann') ** (1/2.)
plot = specgram.plot(yscale='log', ylim=(30, 1400))
plot.colorbar(norm='log', clim=(1e-24, 1e-21), label='Strain ASD')
plot.show()