# Create a lowpass and a highpass filter, and combine them:

from gwpy.signal.filter_design import (
    highpass, lowpass, concatenate_zpks)
hp = highpass(100, 4096)
lp = lowpass(1000, 4096)
zpk = concatenate_zpks(hp, lp)

# Plot the filter:

from gwpy.plotter import BodePlot
plot = BodePlot(zpk, sample_rate=4096)
plot.show()
