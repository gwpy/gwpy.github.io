"""
############################
Simple coherence spectrogram
############################


This example shows the time-variation :ref:`spectrogram <gwpy-spectrogram>`
of the estimated coherence between the differential-arm length servo
control loop error signal for LIGO-Hanford (``H1:LSC-DARM_IN1_DQ``) and
the motion of an optical periscope used to direct the main laser beam into
the Hanford interferometer, around the time of |GW170814|.

.. code-block:: shell
    
    gwpy-plot coherencegram \\
        --chan H1:LSC-DARM_IN1_DQ H1:PEM-CS_ACC_PSL_PERISCOPE_X_DQ \\
        --start 1186741560 \\
        --duration 600 \\
        --nds2-server nds.gwosc.org \\
        --interactive
"""

# %%
# The same command can be executed directly in Python as:

from gwpy.cli.gwpy_plot import main
main([
    'coherencegram',
    '--chan', 'H1:LSC-DARM_IN1_DQ', 'H1:PEM-CS_ACC_PSL_PERISCOPE_X_DQ',
    '--start', '1186741560',
    '--duration', '600',
    '--nds2-server', 'nds.gwosc.org',
    '--interactive',
])