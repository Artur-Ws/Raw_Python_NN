import numpy as np
import matplotlib.pyplot as plt
import math


def spiral(n_points, n_clases, param1=4, param2=4, noise=0.1):
    """
    Function for 2D spiral dataset generation, with given number of classes and samples.
    :param n_points: number of points for each class
    :param n_clases: number of classes
    :param param1: first parameter for theta generation
    :param param2: second parameter for theta generation
    :param noise: level of noise. 0 for smooth, default is 0.1
    :return:
    """
    x = np.zeros((n_points * n_clases, 2))
    y = np.zeros(n_points * n_clases)
    pi = math.pi

    for i in range(n_clases):
        ix = range(n_points*i, n_points*(i+1))
        r = np.linspace(0, 1, n_points)
        t = np.linspace(i*param1, (i+1)*param2, n_points) + np.random.randn(n_points)*noise
        x[ix] = np.c_[r*np.sin(t), r*np.cos(t)]
        y[ix] = i
    plt.scatter(x[:, 0], x[:, 1], c=y)
    plt.show()