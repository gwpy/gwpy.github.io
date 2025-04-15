"""
###############
Simple spectrum
###############


This example shows a simple spectrum (power spectral density) of strain
data from the LIGO-Livingston detector around the time of GW200129_065458
(see |GWTC-3l|_ for full details).

.. code-block:: shell
    
    gwpy-plot spectrum \\
        --gwosc \\
        --ifo L1 \\
        --start 1264316100 \\
        --duration 32 \\
        --interactive
"""

# %%
# The same command can be executed directly in Python as:

from gwpy.cli.gwpy_plot import main
main([
    'spectrum',
    '--gwosc',
    '--ifo', 'L1',
    '--start', '1264316100',
    '--duration', '32',
    '--interactive',
])