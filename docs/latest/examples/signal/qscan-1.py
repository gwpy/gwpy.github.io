from gwosc import datasets
from gwpy.timeseries import TimeSeries
gps = datasets.event_gps('GW170817')
data = TimeSeries.fetch_open_data('L1', gps-34, gps+34, tag='C00')