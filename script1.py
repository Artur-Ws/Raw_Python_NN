import numpy as np

### 1 ### Perform adding row vector to a square matrix
ones = np.ones([4, 4])
row1 = [2, 2, 2, 2]
row_to_matrix = ones + row1

print("Added row vector: ", row1, "\nto matrix: \n", ones,
      "\n and result is:\n", row_to_matrix)
# Vector is added to each row of matrix, as shown



