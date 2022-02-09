import numpy as np
import random


class Perceptron():

    def __init__(self, input_list, weight_list, bias=0):
        self.input_list  = input_list
        self.weight_list = weight_list
        self.bias        = bias
        # Check whether there is same number of inputs and weights
        self.check_data()

    def check_data(self):

        if len(self.input_list) != len(self.weight_list):
            print(self)
            raise ValueError('input_list and weight_list must have the same number of elements!')

    def output(self):

        output_value = self.bias
        for input_value, weight in zip(self.input_list, self.weight_list):
            output_value += input_value * weight
        return output_value


input_list = (1, 2, 3, 4)
weights = (0.2, 0.6, -0.3, 0.9)
bias = 0
x = Perceptron(input_list, weights, bias)

print(x.output())