"""
########################
High-resolution spectrum
########################


This example shows a high-resolution spectrum (power spectral density) of
the strain data from LIGO-Livingston around GW200129_065458
(see |GWTC-3l|_ for full details).

.. code-block:: shell
    
    gwpy-plot spectrum \\
        --gwosc \\
        --ifo L1 \\
        --start 1264315518 \\
        --duration 1024 \\
        --secpfft 64 \\
        --xmin 10 \\
        --xmax 1600 \\
        --interactive
"""

# %%
# The same command can be executed directly in Python as:

from gwpy.cli.gwpy_plot import main
main([
    'spectrum',
    '--gwosc',
    '--ifo', 'L1',
    '--start', '1264315518',
    '--duration', '1024',
    '--secpfft', '64',
    '--xmin', '10',
    '--xmax', '1600',
    '--interactive',
])