plot = l1spec.plot(figsize=(12, 5))
ax = plot.gca()
ax.set_yscale('log')
ax.set_ylim(15, 500)
ax.set_title('LIGO-Livingston sensitivity to BNS around GW170817')
ax.set_epoch(1187008882)  # <- set 0 on plot to GW170817
ax.colorbar(cmap='cividis', clim=(0, 16),
            label='BNS range amplitude spectral density '
                  r'[Mpc/$\sqrt{\mathrm{Hz}}$]')
plot.show()