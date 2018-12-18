import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

number_of_corners = 150
divisor = float(10)

def get_cor_point(divisions, multiple, current):
    return np.cos(np.pi+(2*np.pi/divisions)*current*multiple), np.sin((2*np.pi/divisions)*current*multiple)

def connect_points(multiple, number_divisions = 10):
    points = []
    x = []
    y = []
    for i in range(number_divisions):
        xy1 = get_cor_point(number_divisions, 1, i)
        xy2 = get_cor_point(number_divisions, multiple, i)
        x += [xy1[0], xy2[0]],
        y += [xy1[1], xy2[1]],
    points = [x,y]
    return points

def plt_cont():
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    def update(i):
        ax.clear()
        points = connect_points(i/divisor, number_of_corners)
        for i in range(len(points[0])):
            ax.plot(points[0][i],
            points[1][i], 'ro-')
    a = anim.FuncAnimation(fig, update, frames=1000, repeat=False, interval = 10)
    plt.show()
    
plt_cont()
