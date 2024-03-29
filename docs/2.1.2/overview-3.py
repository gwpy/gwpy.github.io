from gwpy.plot import Plot
plot = Plot(figsize=(12, 4))
ax = plot.add_subplot(xscale='auto-gps')
ax.plot(h1b, color='gwpy:ligo-hanford', label='LIGO-Hanford')
ax.plot(l1b, color='gwpy:ligo-livingston', label='LIGO-Livingston')
ax.set_epoch(1126259462.427)
ax.set_xlim(1126259462.2, 1126259462.5)
ax.set_ylim(-1e-21, 1e-21)
ax.set_ylabel('Strain noise')
ax.legend()
plot.show()