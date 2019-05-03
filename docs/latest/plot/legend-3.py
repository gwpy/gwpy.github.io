from matplotlib.legend_handler import HandlerLine2D
from matplotlib.lines import Line2D
class MyHandler(HandlerLine2D):
    def create_artists(self, *args, **kwargs):
        line, marker = super(MyHandler, self).create_artists(
            *args,
            **kwargs,
        )
        line.set_linewidth(4.)
        line.set_linestyle('--')
        return line, marker
fig = pyplot.figure()
ax = fig.gca()
ax.plot(range(10), label='My data')
ax.legend(handler_map={Line2D: MyHandler()}, handlelength=10)
fig.show()
