import numpy as np
var = np.array([1, 2, 4, 2, 5, 2, 5, 6, 7])
x = np.where((var%2)==0)
#print(x)

var1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x1 = np.searchsorted(var1, [5, 6, 7], side="right")
#print(x1)

var_2 = np.array([4, 2, 3, 1, 12, 5, 22, 52, 6, 7])
#print(np.sort(var_2))

var_3 = np.array(["a", "s", "d", "f"])
#print(np.sort(var_3))

var_4 = np.array([[4, 2, 3], [1, 12, 5], [22, 52, 6]])
#print(np.sort(var_4))

var_5 = np.array(["a", "s", "d", "f"])
f = [True, False, False, True]
new_a = var_5[f]
print(np.sort(new_a))
print(type(new_a))