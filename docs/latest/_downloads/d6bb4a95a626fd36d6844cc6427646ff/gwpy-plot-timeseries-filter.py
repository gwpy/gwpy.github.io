"""
###################
Filtered timeseries
###################


This example shows the strain timeseries for the LIGO-Hanford detector
around GW150914 filtered to emphasise the visibility of the known signal
(see :ref:`sphx_glr_examples_signal_gw150914.py` for more detail).

.. code-block:: shell
    
    gwpy-plot timeseries \\
        --gwosc \\
        --ifo H1 \\
        --start 1126259458 \\
        --duration 8 \\
        --xmin 1126259462.1 \\
        --xmax 1126259462.6 \\
        --epoch 1126259462 \\
        --xscale seconds \\
        --lowpass 300 \\
        --highpass 50 \\
        --notch 60 120 \\
        --ylabel 'Strain amplitude' \\
        --geometry 1200x400 \\
        --suptitle 'LIGO-Hanford strain (filtered) around GW150914' \\
        --interactive
"""

# %%
# The same command can be executed directly in Python as:

from gwpy.cli.gwpy_plot import main
main([
    'timeseries',
    '--gwosc',
    '--ifo', 'H1',
    '--start', '1126259458',
    '--duration', '8',
    '--xmin', '1126259462.1',
    '--xmax', '1126259462.6',
    '--epoch', '1126259462',
    '--xscale', 'seconds',
    '--lowpass', '300',
    '--highpass', '50',
    '--notch', '60', '120',
    '--ylabel', 'Strain amplitude',
    '--geometry', '1200x400',
    '--suptitle', 'LIGO-Hanford strain (filtered) around GW150914',
    '--interactive',
])