"""
##################
Simple spectrogram
##################


This example shows a :ref:`spectrogram <gwpy-spectrogram>` of the strain
data from LIGO-Hanford around the time of GW150914.

.. code-block:: shell
    
    gwpy-plot spectrogram \\
        --gwosc \\
        --ifo H1 \\
        --start 1264316116 \\
        --duration 32 \\
        --epoch 1264316116.4 \\
        --ymax 4000 \\
        --interactive
"""

# %%
# The same command can be executed directly in Python as:

from gwpy.cli.gwpy_plot import main
main([
    'spectrogram',
    '--gwosc',
    '--ifo', 'H1',
    '--start', '1264316116',
    '--duration', '32',
    '--epoch', '1264316116.4',
    '--ymax', '4000',
    '--interactive',
])