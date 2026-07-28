import numpy as np
var = np.array([1, 2, 3, 4, 5])
np.random.shuffle(var)
#print(var)
var1 = np.array([1, 2, 3, 4, 2, 5, 2, 6, 7])
x = np.unique(var1, return_index=True, return_counts=True)
#print(x)

var2 = np.array([1, 2, 3, 4, 5, 6])
y = np.resize(var2, (3, 2))
#print(y)
print()
print("Flatten:", y.flatten(order='F'))
print("Ravel:", np.ravel(y, order='A'))
