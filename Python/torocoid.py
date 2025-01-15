import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

RANGE = 0.001
rc = 5.
rm = 3.
rd = 5.

fig, ax = plt.subplots()

line, = ax.plot([], [], "r")
circle, = ax.plot([], [], "b")

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

def init():
    ax.axhline(color="black")
    ax.axvline(color="black")
    return line, circle,

def update(frame):
    sita = np.arange(0., np.pi*6*frame/1000, RANGE)
    x = (rc - rm) * np.cos(sita) + rd * np.cos((rc-rm)/rm*sita)
    y = (rc - rm) * np.sin(sita) - rd * np.sin((rc-rm)/rm*sita)
    line.set_data(x, y)
    circle.set_data(rc*np.cos(sita), rc*np.sin(sita))
    return line, circle,

ani = FuncAnimation(fig, update, frames=range(1000), init_func=init, blit=True)

plt.show()