from gwpy.signal.filter_design import bandpass
from gwpy.plot import BodePlot
zpk = bandpass(40, 1000, 4096, analog=True)
plot = BodePlot(zpk, analog=True, title='40-1000\,Hz bandpass filter')
plot.show()