lho = TimeSeriesDict.get([c.format(ifo='H1') for c in channels],
                         'Feb 13 2015 16:00', 'Feb 14 2015 04:00')
llo = TimeSeriesDict.get([c.format(ifo='L1') for c in channels],
                         'Feb 13 2015 16:00', 'Feb 14 2015 04:00')