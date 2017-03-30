plot = specgram.plot(norm='log', vmin=1e-23, vmax=1e-19)
plot.set_yscale('log')
plot.set_ylim(40, 4000)
plot.add_colorbar(
    label=r'Gravitational-wave amplitude [strain/$\sqrt{\mathrm{Hz}}$]')
plot.show()