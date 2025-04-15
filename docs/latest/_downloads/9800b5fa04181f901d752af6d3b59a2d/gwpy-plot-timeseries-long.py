"""
################################
Time-series of input laser power
################################


This example shows the input laser power (W) for each LIGO Detector
for three hours around GW170817 (data taken from the |GWOSC_AUX_RELEASE|_).

.. code-block:: shell
    
    gwpy-plot timeseries \\
        --chan H1:IMC-PWR_IN_OUT_DQ \\
        --chan L1:IMC-PWR_IN_OUT_DQ \\
        --start 1186736512 \\
        --duration 3hour \\
        --ylabel 'Interferometer input power (W)' \\
        --suptitle 'LIGO input laser power' \\
        --interactive
"""

# %%
# The same command can be executed directly in Python as:

from gwpy.cli.gwpy_plot import main
main([
    'timeseries',
    '--chan', 'H1:IMC-PWR_IN_OUT_DQ',
    '--chan', 'L1:IMC-PWR_IN_OUT_DQ',
    '--start', '1186736512',
    '--duration', '3hour',
    '--ylabel', 'Interferometer input power (W)',
    '--suptitle', 'LIGO input laser power',
    '--interactive',
])