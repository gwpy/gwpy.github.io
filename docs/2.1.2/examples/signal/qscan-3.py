from matplotlib.cm import get_cmap
cmap = get_cmap('viridis')
plot = qgram.tile('time', 'frequency', 'duration', 'bandwidth',
                  color='energy', figsize=[8, 4], linewidth=0.1,
                  edgecolor=cmap(0), antialiased=True)
ax = plot.gca()
ax.set_xscale('seconds')
ax.set_xlim(gps-6, gps+1)
ax.set_epoch(gps)
ax.set_yscale('log')
ax.set_ylim(16, 1024)
ax.set_ylabel('Frequency [Hz]')
ax.grid(True, axis='y', which='both')
ax.colorbar(cmap='viridis', label='Normalized energy', clim=[0, 25])
cmap = get_cmap('viridis')
ax.set_facecolor(cmap(0))
plot.show()