from gwpy.signal import bandpass
from gwpy.plotter import BodePlot
zpk = bandpass(40, 1000, 4096, analog=True)
plot = BodePlot(zpk, analog=True, title='40-1000\,Hz bandpass filter')
plot.show()