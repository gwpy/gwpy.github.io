from scipy import signal
from gwpy.plotter import BodePlot
highpass = signal.butter(4, 10 * (2.0 / 256), btype='highpass')
plot = BodePlot(highpass, sample_rate=256)
