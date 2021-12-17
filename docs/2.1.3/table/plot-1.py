from gwpy.table import EventTable
events = EventTable.read('H1-LDAS_STRAIN-968654552-10.xml.gz', tablename='sngl_burst', columns=['peak', 'central_freq', 'snr'])
plot = events.scatter('peak', 'central_freq', color='snr')
ax = plot.gca()
ax.set_epoch(968654552)
ax.set_yscale('log')
ax.set_ylabel('Frequency [Hz]')
plot.add_colorbar(clim=[1, 10], cmap='YlGnBu', log=True, label='Signal-to-noise ratio (SNR)')
