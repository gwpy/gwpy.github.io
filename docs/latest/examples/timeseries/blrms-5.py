plot = Plot(lho, llo, figsize=(12, 6), sharex=True, yscale='log')
ax1, ax2 = plot.axes
for ifo, ax in zip(('Hanford', 'Livingston'), (ax1, ax2)):
    ax.legend(['X', 'Y', 'Z'])
    ax.text(1.01, 0.5, ifo, ha='left', va='center', transform=ax.transAxes,
            fontsize=18)
ax1.set_ylabel('$1-3$\,Hz motion [nm/s]', y=-0.1)
ax2.set_ylabel('')
ax1.set_title('Magnitude 7.1 earthquake impact on LIGO')
plot.show()