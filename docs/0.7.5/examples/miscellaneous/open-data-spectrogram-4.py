from gwpy.timeseries import TimeSeries
spectrograms = []
for start, end in h1segs.active:
    h1strain = TimeSeries.fetch_open_data('H1', start, end, verbose=True)
    specgram = h1strain.spectrogram(30, fftlength=4) ** (1/2.)
    spectrograms.append(specgram)