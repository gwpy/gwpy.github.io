from gwpy.plotter import SpectrogramPlot
plot = SpectrogramPlot()
ax = plot.gca()
for specgram in spectrograms:
    ax.plot(specgram)
ax.set_epoch('Sep 16 2010')
ax.set_xlim('Sep 16 2010', 'Sep 17 2010')
ax.set_ylim(40, 2000)
ax.set_yscale('log')
ax.set_ylabel('Frequency [Hz]')
ax.set_title('LIGO-Hanford strain data')
plot.add_colorbar(cmap='viridis', clim=(1e-23, 1e-19), log=True,
                  label=r'Strain noise [1/\rtHz]')
plot.add_state_segments(h1segs, ax=ax)
plot.show()