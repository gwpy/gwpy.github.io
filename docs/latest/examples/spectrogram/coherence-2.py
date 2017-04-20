data = TimeSeriesDict.get(['H1:GDS-CALIB_STRAIN',
                           'H1:PEM-CS_ACC_PSL_PERISCOPE_X_DQ'],
                           1126260017, 1126260617)
hoft = data['H1:GDS-CALIB_STRAIN']
acc = data['H1:PEM-CS_ACC_PSL_PERISCOPE_X_DQ']