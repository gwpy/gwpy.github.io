from gwpy.astro import range_spectrogram
l1spec = range_spectrogram(l1, 30, fftlength=4, fmin=15, fmax=500) ** (1./2)