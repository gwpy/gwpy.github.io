h1b = h1.bandpass(50, 250).notch(60).notch(120)
l1b = l1.bandpass(50, 250).notch(60).notch(120)
l1b.t0 += 0.0069 * l1b.xunit
l1b *= -1