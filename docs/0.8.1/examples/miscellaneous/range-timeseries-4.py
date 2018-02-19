from gwpy.plotter.colors import GW_OBSERVATORY_COLORS as GWO_COLORS
plot = h1range.plot(label='LIGO-Hanford', color=GWO_COLORS['H1'])
ax = plot.gca()
ax.plot(l1range, label='LIGO-Livingston', color=GWO_COLORS['L1'])
ax.set_ylabel('Angle-averaged sensitive distance [Mpc]')
ax.set_title('LIGO sensitivity to BNS around GW150914')
ax.set_epoch(1126259462)  # <- set 0 on plot to GW150914
ax.legend()
plot.show()