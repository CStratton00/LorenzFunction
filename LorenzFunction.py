"""
Collin Stratton
CST-305
Topic 5 Project 5: Self-Organized Criticality
Dr. Ricardo Citro

For this project, I used the template code provided in class to create a 
computer program that displays the visualization of the fragmentation 
process as a sequence of save and delete commands are reveived using the 
Lorenz equations

Implementation approach:
- Import code from padlet
- Identify key components in the code to fix/implement
- Implement code to graph the individual equations
"""

# Packages used: numpy, matplotlib, and mplot3d
import numpy as np
import matplotlib.pyplot as plt
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import


def lorenz(x, y, z, s=10, r=10, b=8.0/3.0):
    '''
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    '''
    x_dot = s*(y - x)           # finding the x_dot value from the paramaters
    y_dot = r*x - y - x*z       # finding the y_dot value from the paramaters
    z_dot = x*y - b*z           # finding the z_dot value from the paramaters
    return x_dot, y_dot, z_dot  # return the dot values


dt = 0.01           # step size
num_steps = 10000   # number of steps

# Need one more for the initial values
xs = np.empty(num_steps + 1)            # creates an empty x space
ys = np.empty(num_steps + 1)            # creates an empty y space
zs = np.empty(num_steps + 1)            # creates an empty z space
ts = np.linspace(0, 100, num_steps + 1) # creates an empty t space

# Plot
def plot_Graph(ri):
    # Set initial values
    xs[0], ys[0], zs[0] = (1., 1.01, 1.02)  # set the initial x, y, z values

    # Step through "time", calculating the partial derivatives at the current point
    # and using them to estimate the next point
    for i in range(num_steps):
        x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i], s=10, r=ri, b=8.0/3.0)   # set the x, y, z values from the lorenz function
        xs[i + 1] = xs[i] + (x_dot * dt)                    # input x value into the xspace
        ys[i + 1] = ys[i] + (y_dot * dt)                    # input y value into the xspace
        zs[i + 1] = zs[i] + (z_dot * dt)                    # input z value into the xspace

    fig = plt.figure(1)                                 # create the figure to plot the 3d graph
    ax = fig.gca(projection='3d')                       # create the 3d graph

    ax.plot(xs, ys, zs, lw=0.5)                         # plot the xspace, yspace, and zspace
    ax.set_xlabel("X Axis")                             # x axis label
    ax.set_ylabel("Y Axis")                             # y axis label
    ax.set_zlabel("Z Axis")                             # z axis label
    ax.set_title("Lorenz Attractor with r = %d" % ri)   # title label

    plt.show()          # show graph

    # plot x/t
    plt.title("x/t")    # graph title
    plt.xlabel("t")     # x axis label
    plt.ylabel("x")     # y axis label
    plt.plot(ts, xs)    # plot xspace over time
    plt.legend          # show the legend
    plt.show()          # show the graph

    # plot y/t
    plt.title("y/t")    # graph title
    plt.xlabel("t")     # x axis label
    plt.ylabel("y")     # y axis label
    plt.plot(ts, ys)    # plot yspace over time
    plt.legend          # show the legend
    plt.show()          # show the graph

    # plot z/t
    plt.title("z/t")    # graph title
    plt.xlabel("t")     # x axis label
    plt.ylabel("z")     # y axis label
    plt.plot(ts, zs)    # plot zspace over time
    plt.legend          # show the legend
    plt.show()          # show the graph



plot_Graph(10)      # plot graph at r = 10
plot_Graph(12.5)    # plot graph at r = 12.5
plot_Graph(15)      # plot graph at r = 15