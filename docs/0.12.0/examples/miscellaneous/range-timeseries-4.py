plot = h1range.plot(label='LIGO-Hanford', color='gwpy:ligo-hanford',
                    figsize=(12, 5))
ax = plot.gca()
ax.plot(l1range, label='LIGO-Livingston', color='gwpy:ligo-livingston')
ax.set_ylabel('Angle-averaged sensitive distance [Mpc]')
ax.set_title('LIGO sensitivity to BNS around GW150914')
ax.set_epoch(1126259462)  # <- set 0 on plot to GW150914
ax.legend()
plot.show()