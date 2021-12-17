from gwpy.plot import Plot
plot = Plot()
ax = plot.add_subplot(
    xscale='log', xlim=(10, 1500), xlabel='Frequency [Hz]',
    yscale='log', ylim=(3e-24, 2e-20),
    ylabel=r'Strain noise [1/$\sqrt{\mathrm{Hz}}$]',
)
ax.plot_mmm(median, low, high, color='gwpy:ligo-hanford')
ax.set_title('LIGO-Hanford strain noise variation around GW170817',
             fontsize=16)
plot.show()