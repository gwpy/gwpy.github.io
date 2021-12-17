from gwosc.datasets import event_gps
gps = event_gps("GW150914")
start = int(gps) - 15
end = int(gps) + 15
