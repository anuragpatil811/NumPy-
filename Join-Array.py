import numpy as np
var = np.array([1, 2, 3, 4])
var1 = np.array([9, 8, 7, 6])
ar = np.concatenate((var, var1))
#print(ar)

vr = np.array([[1, 2], [3, 4]])
vr1 = np.array([[9, 8], [7, 6]])
ar_new = np.concatenate((vr, vr1), axis=1)
#print(ar_new)

var_1 = np.array([1, 2, 3, 4])
var_2 = np.array([9, 8, 7, 6])
#a_new = np.concatenate((var_1, var_2))
#a_new = np.vstack((var_1, var_2))
#a_new = np.hstack((var_1, var_2))
a_new = np.dstack((var_1, var_2))
print(a_new)   