import numpy as np
A = np.array([[1, -1, 0, 0, 0],
              [0, 0, 1, -1, 0],
              [0, 1, -1, 0, 0],
              [-1, 0, 0, 0, 1], 
              [0, 0, 0, 1, -1]])
rank = np.linalg.matrix_rank(A)
print("Rank of the given matrix is:", rank)