from gwpy.timeseries import TimeSeries
gwdata = TimeSeries.fetch_open_data('L1', 'Dec 26 2015 03:37',
                                    'Dec 26 2015 03:47', verbose=True)