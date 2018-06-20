import numpy
from gwpy.frequencyseries import FrequencySeries
signal = FrequencySeries(numpy.array([1.]), f0=30, df=noisefd.df)
injfd = noisefd.inject(signal)