from gwpy.plotter.colors import GW_OBSERVATORY_COLORS as GWO_COLORS
plot = lhoasd.plot(color=GWO_COLORS['H1'], label='LIGO-Hanford')
ax = plot.gca()
ax.plot(lloasd, color=GWO_COLORS['L1'], label='LIGO-Livingston')
ax.set_xlim(10, 2000)
ax.set_ylim(5e-24, 1e-21)
plot.show()