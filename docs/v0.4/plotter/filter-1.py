from gwpy.signal import bandpass
from gwpy.plotter import BodePlot
zpk = bandpass(40, 1000, 4096, analog=True)
plot = BodePlot(f, title='40-1000\,Hz bandpass filter')
plot.show()