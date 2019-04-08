inj = injfd.ifft()
plot = Plot(noise, inj, separate=True, sharex=True, sharey=True,
            figsize=(12, 6))
plot.show()