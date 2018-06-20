from astropy.utils.data import get_readable_fileobj
source = 'https://losc.ligo.org/s/events/GW150914/P150914/'
url = '%s/fig2-unfiltered-waveform-H.txt' % source
with get_readable_fileobj(url) as f:
    signal = TimeSeries.read(f, format='txt')
signal.t0 = .5  # make sure this intersects with noise time samples