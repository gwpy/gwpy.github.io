from gwpy.signal.filter_design import bandpass
from gwpy.plot import BodePlot
zpk = bandpass(40, 1000, 4096, analog=False)
plot = BodePlot(zpk, analog=False, sample_rate=4096, title='40-1000 Hz bandpass filter')
plot.show()
