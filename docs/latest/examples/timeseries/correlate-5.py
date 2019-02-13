qaux = waux.q_transform(
    whiten=False,  # already white
    qrange=(4, 150),  # wider Q-transform range
    outseg=(1172489782.57, 1172489783.57),  # region of interest
)
plot = qaux.imshow(figsize=[8, 4])
ax = plot.gca()
ax.set_xscale('seconds')
ax.set_yscale('log')
ax.set_epoch(1172489783.07)
ax.set_ylim(20, 5000)
ax.set_ylabel('Frequency [Hz]')
ax.grid(True, axis='y', which='both')
ax.colorbar(cmap='viridis', label='Normalized energy', clim=[0, 25])
plot.show()