import numpy as np
import random


class Perceptron:
    """
    Perceptron object stores inputs, weights, and bias data
    for one perceptron in layer. It has also output method, that calculates
    final output of that particular data cell
    """

    def __init__(self, input_data=[], weight_list=[], bias=0):
        self.input_data = input_data
        self.weight_list = weight_list
        self.bias = bias
        # Check whether there is same number of inputs and weights
        self.check_data()

    def check_data(self):

        if len(self.input_data) != len(self.weight_list):
            print(self)
            raise ValueError('input_list and weight_list must have the same number of elements!')

    def output(self):

        output_value = self.bias
        for input_value, weight in zip(self.input_data, self.weight_list):
            output_value += input_value * weight
        return output_value


def calculate_layer(*args):
    """
    Function gets any number of perceptron obiects in layer,
    and calculates output list of that layer.
    """
    output_list = []
    for arg in args:
        if type(arg) != type(Perceptron()):
            print("method <calculate_layer> accepts only 'perceptron' objects "
                  "as an arguments.")
        else:
            output_list.append(arg.output())
    return output_list


input_list = [1, 2, 3, 4]
weights = [[0.2, 0.6, -0.3, 0.9],
           [0.2, 0.6, 0.2, -0.9],
           [-0.4, 0.2, -0.1, 0.2]]
bias = [0, 0, 0]

x = Perceptron(input_list, weights[0], bias[0])
y = Perceptron(input_list, weights[1], bias[1])
z = Perceptron(input_list, weights[2], bias[2])

print(type(x))
print(calculate_layer(x, y, z))
