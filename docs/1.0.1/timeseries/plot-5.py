combined = TimeSeriesDict()
combined['L1'] = l1hoft
combined['H1'] = h1hoft
plot = combined.plot()
plot.gca().legend()
plot.show()
