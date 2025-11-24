import numpy as np
#**Shape**
var = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
#print(var)
#print()
#print(var.shape)

var1 = np.array([1, 2, 3, 4], ndmin=4)
#print(var1)
#print(var1.ndim)
#print()
#print(var1.shape)

#**Reshape**
var2 = np.array([1, 2, 3, 4, 5, 6])
#print(var2.ndim)
#x = var2.reshape(2, 3)
#print(x)
#print(x.ndim)

var3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(var3.ndim)
x1 = var3.reshape(2, 3, 2)
print(x1)
print(x1.ndim)
print()
one= x1.reshape(-1)
print(one)
print(one.ndim)