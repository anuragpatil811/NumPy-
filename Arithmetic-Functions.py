import numpy as np
var = np.array([1, 2, 3, 4, 5, 3, 2])
#print("Min:", np.min(var), np.argmin(var))
#print("Max:", np.max(var), np.argmax(var))
#print("sqrt:", np.sqrt(var))
var1 = np.array([[2, 1, 3], [9, 5, 6]])
#print(np.min(var1, axis=0))

var2 = np.array([1, 2, 3])
#print(np.sin(var2))
#print(np.cos(var2))
print(np.cumsum(var2))