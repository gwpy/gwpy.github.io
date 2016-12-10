bits = [
    'Summary state',
    'State 1 damped',
    'Stage 1 isolated',
    'Stage 2 damped',
    'Stage 2 isolated',
    'Master switch ON',
    'Stage 1 WatchDog OK',
    'Stage 2 WatchDog OK',
]

data = StateVector.get('L1:ISI-ETMX_ODC_CHANNEL_OUT_DQ', 'May 22 2014 14:00', 'May 22 2014 15:00', bits=bits)