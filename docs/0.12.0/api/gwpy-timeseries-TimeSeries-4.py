from gwpy.timeseries import (TimeSeries, StateVector)
print(TimeSeries.fetch_open_data('H1', 1126259446, 1126259478))
# TimeSeries([  2.17704028e-19,  2.08763900e-19,  2.39681183e-19,
# ...,   3.55365541e-20,  6.33533516e-20,
# 7.58121195e-20]
# unit: Unit(dimensionless),
# t0: 1126259446.0 s,
# dt: 0.000244140625 s,
# name: Strain,
# channel: None)
print(StateVector.fetch_open_data('H1', 1126259446, 1126259478))
# StateVector([127,127,127,127,127,127,127,127,127,127,127,127,
# 127,127,127,127,127,127,127,127,127,127,127,127,
# 127,127,127,127,127,127,127,127]
# unit: Unit(dimensionless),
# t0: 1126259446.0 s,
# dt: 1.0 s,
# name: Data quality,
# channel: None,
# bits: Bits(0: data present
# 1: passes cbc CAT1 test
# 2: passes cbc CAT2 test
# 3: passes cbc CAT3 test
# 4: passes burst CAT1 test
# 5: passes burst CAT2 test
# 6: passes burst CAT3 test,
# channel=None,
# epoch=1126259446.0))

# For the `StateVector`, the naming of the bits will be
# ``format``-dependent, because they are recorded differently by LOSC
# in different formats.

# For events published in O2 and later, LOSC typically provides
# multiple data sets containing the original (``'C00'``) and cleaned
# (``'CLN'``) data.
# To select both data sets and plot a comparison, for example:

orig = TimeSeries.fetch_open_data('H1', 1187008870, 1187008896,
                                  tag='C00')
cln = TimeSeries.fetch_open_data('H1', 1187008870, 1187008896,
                                 tag='CLN')
origasd = orig.asd(fftlength=4, overlap=2)
clnasd = cln.asd(fftlength=4, overlap=2)
plot = origasd.plot(label='Un-cleaned')
ax = plot.gca()
ax.plot(clnasd, label='Cleaned')
ax.set_xlim(10, 1400)
ax.set_ylim(1e-24, 1e-20)
ax.legend()
plot.show()
