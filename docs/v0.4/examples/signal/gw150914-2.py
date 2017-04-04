from gwpy.signal import filter_design
bp = filter_design.bandpass(50, 250, data.sample_rate)