import numpy as np
from random_matrix import random_matrix

### 1 ### Perform adding row vector to a square matrix
ones = np.ones([4, 4])
row1 = [1, 2, 3, 4]
row_to_matrix = ones + row1
print("Added row vector: ", row1, "\nto matrix: \n",
      ones, "\n and result is:\n", row_to_matrix)
# Vector is added to each row of matrix, as shown
# Number of columns (elements) in vector must match number of columns in matrix


### 2 ### Transposition of matrix with numpy
original = np.array([[1, 2, 3, 4],
                     [5, 6, 7, 8]])
after_trans = original.T
print("\nMatrix before transposition:\n", original,
      "\nMatrix after transposition:\n", after_trans)
# In general each row is transformed into column, and column into row
# Matrix does not have to be homologous to perform transposition


### 3 ### Dot product of vectors
vect1 = [1, 2, 3, 4]
vect2 = np.ones([4])*2
dot_prod = np.dot(vect1, vect2)
print("\nDot product of vectors: ", vect1, " and ", vect2,
      "  Is equal: ", dot_prod)
# Dot product takes elements with the same index,
# then multiplicate it and adds to each others.
# It looks like: dot([a1,a2,..,an],[b1,b2,..,bn}) equals: (a1*b1 + a2*b2 +..+ an*bn)
# Both vectors must be the same size


### 4 ### Matrix product
matrix1 = np.array([[2, 3, 4, 5],
                    [6, 7, 8, 9]])
matrix2 = np.array([[0, 1, 1],
                    [2, 3, 2],
                    [4, 5, 3],
                    [6, 7, 4]])
matrix_prod = np.dot(matrix1, matrix2)
print("\nMatrix product of matrices:\n", matrix1, "\nand\n",
      matrix2, "\nequals:\n", matrix_prod)
# Number of columns in first matrix must be the same as number of rows in second one,
# shape of resulting matrix is determined by number of rows in first matrix
# and number of columns in second one. Here shape (2,4)X(4,3) - 4=4 so we can perform
# a matrix product and result will have a shape of (2,3)


### 5 ### Batch of data to layer of neurons - matrix product part.2
input_set = random_matrix(10, 4)
weight_set = random_matrix(3, 4, [-5, 5])
# Batch of 10 samples data with 4 features and layer of 3 neurons with 4 weights each
# first weight set need to be transposed to perform matrix product
trans_weight_set = weight_set.T
layer_output = np.dot(input_set, trans_weight_set)
print(layer_output.shape)
# Shape of layer_output is (10, 3) which means there is a 10 sets
# of 3 neuron outputs, one for each particular feature set


### 6 ### Building a network with hidden layer
feature_set = random_matrix(10, 5)
weight_set_1 = random_matrix(4, 5, [-5, 5])
bias_set_1 = random_matrix(1, 4, [0, 5])
weight_set_2 = random_matrix(3, 4, [-5, 5])
bias_set_2 = random_matrix(1, 3, [0, 5])
#
first_layer_output = np.dot(feature_set, weight_set_1.T) + bias_set_1
# First layer output has a shape of (10, 4) thus we have 4 neurons here
# now it can be passed to the second layer as a input dataset
# second layer has 3 neurons and set of 4 weights for each neuron,
# because previous layer has 4 neurons, thus 4 inputs to the second layer
second_layer_output = np.dot(first_layer_output, weight_set_2.T) + bias_set_2



