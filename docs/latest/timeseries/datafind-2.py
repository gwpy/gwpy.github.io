from gwpy.timeseries import TimeSeriesDict
data = TimeSeriesDict.get(
    ["H1:ISI-GND_STS_ITMY_Z_BLRMS_30M_100M.rms,s-trend",
     "H1:ISI-GND_STS_ETMY_Z_BLRMS_30M_100M.rms,s-trend"],
    "July 22 2021 12:00",
    "July 22 2021 14:00",
)
plot = data.plot(ylabel="Ground motion [nm/s]")
plot.show()
