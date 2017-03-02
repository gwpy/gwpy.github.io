from gwpy.table import EventTable
events = EventTable.read(
    '../../gwpy/tests/data/H1-LDAS_STRAIN-968654552-10.xml.gz',
    format='ligolw.sngl_burst', columns=['time', 'snr'])