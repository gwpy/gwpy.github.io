from gwpy.timeseries import TimeSeries
data = TimeSeries.fetch_open_data('L1', 1126259446, 1126259478)
from matplotlib import pyplot as plt
plt.plot(data)
plt.show()
