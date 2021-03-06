plot = variance.plot(norm='log', vmin=.5, cmap='plasma')
ax = plot.gca()
ax.grid()
ax.set_xlim(20, 1500)
ax.set_ylim(1e-24, 1e-20)
ax.set_xlabel('Frequency [Hz]')
ax.set_ylabel(r'[strain/\rtHz]')
ax.set_title('LIGO-Livingston sensitivity variance')
plot.show()