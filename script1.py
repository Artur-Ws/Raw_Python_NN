import numpy as np

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
