size = min(gndfft.size, hpifft.size)
tf = hpifft[:size] / gndfft[:size]