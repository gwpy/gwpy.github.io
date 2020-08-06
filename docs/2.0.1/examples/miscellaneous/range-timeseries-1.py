from gwpy.timeseries import TimeSeries
h1 = TimeSeries.fetch_open_data('H1', 1187006834, 1187010930, tag='C02')
l1 = TimeSeries.fetch_open_data('L1', 1187006834, 1187010930, tag='C02')