import numpy as np


class LayerDense:
    """A class for dense layer of neurons instantiate"""

    def __init__(self, inputs, neurons):
        self.inputs = inputs
        self.neurons = neurons
        self.weights = np.random.randn(inputs, neurons) * 0.01
        self.biases = np.zeros(1, neurons)

    def forward(self, ):
        pass
