hp = white.highpass(4)
displacement = hp.zpk([100]*5, [1]*5, 1e-10)