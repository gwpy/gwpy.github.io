from gwpy.plotter import BodePlot
plot = BodePlot(zpk, sample_rate=4096)
plot.show()