from gwpy.astro import range_timeseries
h1range = range_timeseries(h1, 30, fftlength=4, fmin=10)
l1range = range_timeseries(l1, 30, fftlength=4, fmin=10)