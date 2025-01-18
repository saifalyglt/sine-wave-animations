from manim import *

class SineWave(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[0, 4 * PI, PI],
            y_range=[-1.5, 1.5, 0.5],
            x_length=10,
            y_length=4,
            tips=False,
        ).to_edge(DOWN)

        # Create sine wave function
        sine_wave = axes.plot(lambda x: np.sin(x), color=BLUE, x_range=[0, 4 * PI])

        # Add axes and sine wave to the scene
        self.add(axes)
        self.play(Create(sine_wave), run_time=3)
        self.wait()

        # Animate a dot moving along the sine wave
        dot = Dot().move_to(axes.i2gp(0, sine_wave))
        self.add(dot)

        self.play(
            MoveAlongPath(dot, sine_wave),
            run_time=5,
            rate_func=linear
        )
        self.wait()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Data for the sine wave
x = np.linspace(0, 4 * np.pi, 1000)
y = np.sin(x)

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim(0, 4 * np.pi)
ax.set_ylim(-1.5, 1.5)
line, = ax.plot(x, y, lw=2, color='blue')
dot, = ax.plot([], [], 'ro')  # Moving dot

# Update function for animation
def update(frame):
    dot.set_data(x[frame], y[frame])
    return dot,

# Create animation
ani = FuncAnimation(fig, update, frames=len(x), interval=10, blit=True)

plt.show()

