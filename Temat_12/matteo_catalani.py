from matplotlib import pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation 
   
# initializing a figure in which the graph will be plotted
fig = plt.figure() 
# marking the x-axis and y-axis
axis = plt.axes(xlim =(0, 4), ylim =(-2, 2)) 
# initializing a line variable
line, = axis.plot([], [], lw = 3)
dot, = axis.plot([], [], 'ro', markersize=30)
   
# data which the line will contain (x, y)
def init(): 
    line.set_data([], [])
    dot.set_data([], [])
    return line, dot,
   
def animate(i):
    x = np.linspace(0, 4, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)

    dot_x = 0
    dot_y = np.sin(2 * np.pi * (-0.01 * i))
    dot.set_data(dot_x, dot_y)

    return line, dot,
   
anim = FuncAnimation(fig, animate, init_func = init, frames = 200, interval = 20, blit = True)   
#anim.save('continuousSineWave.mp4', writer = 'ffmpeg', fps = 30)
plt.show()