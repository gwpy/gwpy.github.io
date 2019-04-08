whoft = hoft.whiten(8, 4)
waux = aux.whiten(8, 4)
 # We can now cross-correlate these channels:
mfilter = waux.crop(1172489782.57, 1172489783.57)
snr = whoft.correlate(mfilter).abs()