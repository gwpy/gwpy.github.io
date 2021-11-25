from gwosc.datasets import event_gps
from gwpy.timeseries import TimeSeries
gps = event_gps("GW170814")
start = int(gps) - 100
end = int(gps) + 100
data = TimeSeries.get("H1:IMC-PWR_IN_OUT_DQ", start, end, host="losc-nds.ligo.org")
plot = data.plot(ylabel="Power [W]")
plot.show()
