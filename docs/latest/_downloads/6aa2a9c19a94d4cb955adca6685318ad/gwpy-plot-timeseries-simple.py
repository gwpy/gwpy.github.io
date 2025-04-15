"""
#################
Simple timeseries
#################

This example shows the strain timeseries for the LIGO-Hanford detector around GW150914.

.. code-block:: shell
    
    gwpy-plot timeseries \\
        --gwosc \\
        --ifo H1 \\
        --start 1126259457 \\
        --suptitle 'LIGO-Hanford strain around GW150914' \\
        --interactive
"""

# %%
# The same command can be executed directly in Python as:

from gwpy.cli.gwpy_plot import main
main([
    'timeseries',
    '--gwosc',
    '--ifo', 'H1',
    '--start', '1126259457',
    '--suptitle', 'LIGO-Hanford strain around GW150914',
    '--interactive',
])