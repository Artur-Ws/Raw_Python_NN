import numpy as np
import random


def random_matrix(rows=1, columns=1, scope=None):
    """
    Generates a matrix with given number of rows and columns.
    Each element in this matrix will have a random value between given scope
    """
    if scope is None:
        scope = [-1, 1]
    range = scope[1] - scope[0]
    matrix = np.zeros([rows, columns])
    x, y = 0, 0
    for row in matrix:
        for column in row:
            matrix[x, y] = scope[0] + random.random() * range
            y += 1
        y = 0
        x += 1
    return matrix



