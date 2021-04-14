"""
Collin Stratton
CST-305
Topic 7 Project 7: Code Errors and the Butterfly Effect
Dr. Ricardo Citro

For this project, I used the template code provided in class to create a 
computer program that displays the visualization of the fragmentation 
process as a sequence of save and delete commands are reveived using the 
Lorenz equations

Implementation approach:
- Identify key components in the code to fix/implement
- Implement code to graph the individual equations
"""

# Packages used: numpy, matplotlib, and mplot3d
import numpy as np
import matplotlib.pyplot as plt


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
def plot_Graph(si, ri, bi):
    # Set initial values
    xs[0], ys[0], zs[0] = (1., 1.01, 1.02)  # set the initial x, y, z values

    # Step through "time", calculating the partial derivatives at the current point
    # and using them to estimate the next point
    for i in range(num_steps):
        x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i], s = si, r = ri, b = bi)   # set the x, y, z values from the lorenz function
        xs[i + 1] = xs[i] + (x_dot * dt)    # input x value into the xspace
        ys[i + 1] = ys[i] + (y_dot * dt)    # input y value into the xspace
        zs[i + 1] = zs[i] + (z_dot * dt)    # input z value into the xspace

    fig = plt.figure(1)             # create the figure to plot the 3d graph
    ax = fig.gca(projection='3d')   # create the 3d graph

    ax.plot(xs, ys, zs, lw=0.5)         # plot the xspace, yspace, and zspace
    ax.set_xlabel("X Axis")             # x axis label
    ax.set_ylabel("Y Axis")             # y axis label
    ax.set_zlabel("Z Axis")             # z axis label
    ax.set_title("Lorenz Attractor")    # title label

    plt.show()          # show graph

userInput = int(input("Run Lorenz Function (0|1): "))       # check to see if the user wants to run the lorenz function, 0 for no 1 for yes
while(userInput == 1):                                      # while the user wants to run the lorenz function
    s = float(input("Input s value: "))                     # grab the s value from the user
    r = float(input("Input r value: "))                     # grab the r value from the user
    b = float(input("Input b value: "))                     # grab the b value from the user

    plot_Graph(s, r, b)                                     # plot the graph with the user values
    userInput = int(input("Run Lorenz Function (0|1): "))   # check to see if the user wants to run the lorenz function, 0 for no 1 for yes
