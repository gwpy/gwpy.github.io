h1b = h1.bandpass(50, 250).notch(60).notch(120)
l1b = l1.bandpass(50, 250).notch(60).notch(120)
l1b.shift('6.9ms')
l1b *= -1