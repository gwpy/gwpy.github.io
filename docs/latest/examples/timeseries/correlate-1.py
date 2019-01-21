from gwpy.timeseries import TimeSeries
hoft = TimeSeries.get('L1:GDS-CALIB_STRAIN', 1172489751, 1172489815)
aux = TimeSeries.get('L1:PSL-ISS_PDA_REL_OUT_DQ', 1172489751, 1172489815)