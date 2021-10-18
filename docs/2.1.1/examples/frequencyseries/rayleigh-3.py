from gwpy.plot import Plot
plot = Plot(gwdata.asd(2, 1), rayleigh, geometry=(2, 1), sharex=True,
            xscale='log', xlim=(30, 1500))
asdax, rayax = plot.axes
asdax.set_yscale('log')
asdax.set_ylim(5e-24, 1e-21)
asdax.set_ylabel(r'[strain/$\sqrt{\mathrm{Hz}}$]')
rayax.set_ylim(0, 2)
rayax.set_ylabel('Rayleigh statistic')
asdax.set_title('Sensitivity of LIGO-Livingston around GW151226', fontsize=20)
plot.show()