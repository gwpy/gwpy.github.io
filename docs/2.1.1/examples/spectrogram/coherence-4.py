plot = coh.plot()
ax = plot.gca()
ax.set_ylabel('Frequency [Hz]')
ax.set_yscale('log')
ax.set_ylim(10, 8000)
ax.set_title(
    'Coherence between PSL periscope motion and LIGO-Hanford strain data',
)
ax.grid(True, 'both', 'both')
ax.colorbar(label='Coherence', clim=[0, 1], cmap='plasma')
plot.show()