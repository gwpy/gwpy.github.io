specgram = white.spectrogram2(fftlength=1/16., overlap=15/256.) ** (1/2.)
specgram = specgram.crop_frequencies(20)  # drop everything below highpass