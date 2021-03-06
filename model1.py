import numpy as np
import matplotlib.pyplot as plt
import math
from data_generation import spiral


class LayerDense:
    """A class for dense layer of neurons instantiate"""

    def __init__(self, n_inputs, n_neurons):
        self.inputs = n_inputs
        self.neurons = n_neurons
        self.weights = np.random.randn(n_inputs, n_neurons) * 0.01
        self.biases = np.zeros(1, n_neurons)

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


spiral(100, 3, noise=0.5, color=False)
