"""
#####################
Spectrum at two times
#####################


This example plots the spectrum (power spectral density) of strain data
from both LIGO-Hanford and LIGO-Livingston for two different GPS times
(around GW150914 and GW170817).

.. code-block:: shell
    
    gwpy-plot spectrum \\
        --gwosc \\
        --ifo H1 L1 \\
        --start 1126259446 \\
        --start 1187008866 \\
        --duration 32 \\
        --interactive
"""

# %%
# The same command can be executed directly in Python as:

from gwpy.cli.gwpy_plot import main
main([
    'spectrum',
    '--gwosc',
    '--ifo', 'H1', 'L1',
    '--start', '1126259446',
    '--start', '1187008866',
    '--duration', '32',
    '--interactive',
])