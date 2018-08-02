plot = specgram.imshow(norm='log', vmin=5e-24, vmax=1e-19)
ax = plot.gca()
ax.set_yscale('log')
ax.set_ylim(10, 2000)
ax.colorbar(
    label=r'Gravitational-wave amplitude [strain/$\sqrt{\mathrm{Hz}}$]')
plot.show()