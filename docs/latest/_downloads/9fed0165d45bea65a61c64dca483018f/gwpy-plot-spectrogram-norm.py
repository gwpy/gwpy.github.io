"""
######################
Normalised spectrogram
######################


This example shows a normalised :ref:`spectrogram <gwpy-spectrogram>` of
the strain data from LIGO-Hanford around the time of GW150914.

.. code-block:: shell
    
    gwpy-plot spectrogram \\
        --gwosc \\
        --ifo L1 \\
        --start 1264315518 \\
        --duration 1024 \\
        --norm \\
        --cmap Spectral_r \\
        --imin .25 \\
        --imax 4 \\
        --interactive
"""

# %%
# The same command can be executed directly in Python as:

from gwpy.cli.gwpy_plot import main
main([
    'spectrogram',
    '--gwosc',
    '--ifo', 'L1',
    '--start', '1264315518',
    '--duration', '1024',
    '--norm',
    '--cmap', 'Spectral_r',
    '--imin', '.25',
    '--imax', '4',
    '--interactive',
])