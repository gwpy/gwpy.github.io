gooddata = TimeSeries.get('L1:PSL-ISS_PDB_OUT_DQ', goodtime, goodtime+duration)
baddata = TimeSeries.get('L1:PSL-ISS_PDB_OUT_DQ', badtime, badtime+duration)