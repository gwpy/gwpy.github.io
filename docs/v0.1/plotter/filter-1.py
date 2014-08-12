from scipy import signal
from gwpy.plotter import BodePlot
highpass = signal.butter(4, 10 * (2. * signal.np.pi), btype='highpass',
# analog=True)
plot = BodePlot(highpass)
