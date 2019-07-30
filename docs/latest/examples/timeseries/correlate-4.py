plot = snr.crop(1172489782.07, 1172489784.07).plot()
plot.axes[0].set_epoch(1172489783.07)
plot.axes[0].set_ylabel('Signal-to-noise ratio', fontsize=16)
plot.show()