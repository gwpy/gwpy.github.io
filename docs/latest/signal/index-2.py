from gwpy.signal import bandpass
from gwpy.plotter import BodePlot
f = bandpass(40, 1000, data.sample_rate)
plot = BodePlot(f, sample_rate=data.sample_rate,
                title='40-1000\,Hz bandpass filter')
plot.show()