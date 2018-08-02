from gwpy.plot import Plot
plot = Plot(figsize=(12, 6))
ax = plot.gca()
for specgram in spectrograms:
    ax.imshow(specgram)
ax.set_xscale('auto-gps', epoch='Sep 16 2010')
ax.set_xlim('Sep 16 2010', 'Sep 17 2010')
ax.set_ylim(40, 2000)
ax.set_yscale('log')
ax.set_ylabel('Frequency [Hz]')
ax.set_title('LIGO-Hanford strain data')
ax.colorbar(cmap='viridis', norm='log', clim=(1e-23, 1e-19),
            label=r'Strain noise [1/\rtHz]')
plot.add_segments_bar(h1segs)
plot.show()