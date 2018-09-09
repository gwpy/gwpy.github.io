from gwpy.timeseries import TimeSeries
gwdata = TimeSeries.fetch('H1:LDAS-STRAIN', 'September 16 2010 06:40',
                          'September 16 2010 06:50')
specgram = gwdata.spectrogram(20, fftlength=8, overlap=4) ** (1/2.)
