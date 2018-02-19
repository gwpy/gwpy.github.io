from gwpy.table import EventTable
events = EventTable.read('H1-LDAS_STRAIN-968654552-10.xml.gz',
                         tablename='sngl_burst', columns=['time', 'snr'])