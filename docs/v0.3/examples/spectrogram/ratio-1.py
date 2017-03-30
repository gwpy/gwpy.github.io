from gwpy.timeseries import TimeSeries
gwdata = TimeSeries.get('H1:LDAS-STRAIN', 'September 16 2010 06:40', 'September 16 2010 06:50')
specgram = gwdata.spectrogram(5, fftlength=2, overlap=1) ** (1/2.)