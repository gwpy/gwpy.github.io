from gwpy.timeseries import TimeSeries
gwdata = TimeSeries.fetch('H1:LDAS-STRAIN', 'September 16 2010 06:40',
                          'September 16 2010 06:50')
spectrum = gwdata.asd(8, 4)
