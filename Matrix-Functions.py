import numpy as np
var = np.matrix([[1, 2, 3], [4, 5, 6]])
#print(var)
print()

#TRANSPOSE
#print(np.transpose(var))
print()
#print(var.T)

#SWAPAXES
#print(np.swapaxes(var, 0, 1))

var3 = np.matrix([[1, 2], [3, 4]])
#print(np.linalg.inv(var3))

var4 = np.matrix([[1, 2], [3, 4]])
#print(np.linalg.matrix_power(var4, 2))
#print()
#print(np.linalg.matrix_power(var4, 0))

var5 = np.matrix([[1, 2], [3, 4]])
print(np.linalg.det(var5))