from gwpy.plotter import FrequencySeriesPlot
plot = FrequencySeriesPlot()
ax = plot.gca()
ax.plot_spectrum_mmm(median, min_=min_, max_=max_, color='gwpy:ligo-hanford')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlim(10, 1500)
ax.set_ylim(3e-24, 2e-20)
ax.set_ylabel(r'Strain noise [1/\rtHz]')
ax.set_title('LIGO-Hanford strain noise variation around GW170817',
             fontsize=16)
plot.show()