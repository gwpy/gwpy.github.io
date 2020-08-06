from astropy.utils.data import get_readable_fileobj
url = ("https://www.gw-openscience.org/s/events/GW150914/P150914/"
       "fig2-unfiltered-waveform-H.txt")
with get_readable_fileobj(url) as f:
    signal = TimeSeries.read(f, format='txt')
signal.t0 = .5  # make sure this intersects with noise time samples