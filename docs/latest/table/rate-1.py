from gwpy.table import EventTable
events = EventTable.read('H1-LDAS_STRAIN-968654552-10.xml.gz', tablename='sngl_burst', columns=['peak', 'central_freq', 'snr'])
rate = events.event_rate(1, start=968654552, end=968654562, timecolumn='peak')
plot = rate.plot()
ax = plot.gca()
ax.set_ylabel('Event rate [Hz]')
ax.set_title('LIGO Hanford Observatory event rate for GW100916')
plot.show()
