from gwosc.datasets import event_gps
from gwpy.timeseries import StateVector
gps = event_gps("GW200105_162426")
start = int(gps) - 1000
end = int(gps) + 1000
gw200105_state = StateVector.fetch_open_data("L1", start, end)
print(gw200105_state)
# StateVector([127, 127, 127, ..., 127, 127, 127]
# unit: dimensionless,
# t0: 1262275684.0 s,
# dt: 1.0 s,
# name: Data quality,
# channel: None,
# bits: Bits(0: Passes DATA test
# 1: Passes CBC_CAT1 test
# 2: Passes CBC_CAT2 test
# 3: Passes CBC_CAT3 test
# 4: Passes BURST_CAT1 test
# 5: Passes BURST_CAT2 test
# 6: Passes BURST_CAT3 test,
# channel=None,
# epoch=1262274636.0))
