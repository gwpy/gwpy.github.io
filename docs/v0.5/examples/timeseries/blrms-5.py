plot = TimeSeriesPlot(lho, llo)
ax1, ax2 = plot.axes
for ifo, ax in zip(('H1', 'L1'), (ax1, ax2)):
   ax.legend(['X', 'Y', 'Z'])
   ax.set_yscale('log')
   ax.text(1.02, 0.5, ifo, ha='left', va='center', transform=ax.transAxes,
           fontsize=18)
ax1.set_ylabel('$1-3$\,Hz motion [nm/s]', y=-0.1)
ax1.set_title('Magnitude 7.1 earthquake impact on LIGO')
plot.show()