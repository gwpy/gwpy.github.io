from gwpy.timeseries import TimeSeries
gwdata = TimeSeries.fetch_open_data(
    'H1', 'September 16 2010 07:00', 'September 16 2010 07:10',
    verbose=True)