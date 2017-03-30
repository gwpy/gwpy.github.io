plot = TimeSeriesPlot(lho, llo)
for ifo, ax in zip(['H1', 'L1'], plot.axes):
   ax.legend(['X', 'Y', 'Z'])
   ax.yaxis.set_label_position('right')
   ax.set_ylabel(ifo, rotation=0, va='center', ha='left')
   ax.set_yscale('log')
plot.text(0.1, 0.5, '$1-3$\,Hz motion [nm/s]', rotation=90, fontsize=24,
          ha='center', va='center')
plot.axes[0].set_title('Magnitude 7.1 earthquake impact on LIGO', fontsize=24)
plot.show()