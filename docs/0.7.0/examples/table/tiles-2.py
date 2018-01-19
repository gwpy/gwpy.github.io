plot = events.plot('time', 'central_freq', 'duration', 'bandwidth',
                   color='snr')
ax = plot.gca()
ax.set_yscale('log')
ax.set_ylabel('Frequency [Hz]')
ax.set_epoch(968654552)
ax.set_xlim(968654552, 968654552+10)
ax.set_title('LIGO-Hanford event tiles for HW100916')
plot.add_colorbar(clim=[1, 8], cmap='YlGnBu',
                  label='Signal-to-noise ratio (SNR)')
plot.show()