from gwpy.table import EventTable
events = EventTable.read(
    'H1-LDAS_STRAIN-968654552-10.xml.gz', format='ligolw.sngl_burst',
    columns=['time', 'central_freq', 'snr'])