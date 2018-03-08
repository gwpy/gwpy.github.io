plot = b.crop(1126259462, 1126259462.6).plot(
    figsize=[12, 4], color='gwpy:ligo-hanford')
ax = plot.gca()
ax.set_title('LIGO-Hanford strain data around GW150914')
ax.set_ylabel('Amplitude [strain]')
ax.set_epoch(1126259462.427)
plot.show()