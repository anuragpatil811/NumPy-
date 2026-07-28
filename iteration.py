import numpy as np
var = np.array([9, 8, 7, 6, 5, 4])
#print(var)
print()
#for i in var:
#    print(i)
var1 = np.array([[1, 2, 3, 4], [1,2, 3, 4]])
"""""
print(var1)
print()
for j in var1:
    print(j)
print()
for k in var1:
    for l in k:
        print(l)
"""
var3 = np.array([[[9,8, 7, 6], [1, 2, 3, 4]]])
print(var3)
print(var3.ndim)
print()
"""""
for i in var3:
    for j in i:
        for k in j:
            print(k)
"""
for i in np.nditer(var3, flags=['buffered'], op_dtypes=["S"]):
    print(i)

var4 = np.array([[[9,8, 7, 6], [1, 2, 3, 4]]])
print(var4)
print(var4.ndim)
print()
for i, d in np.ndenumerate(var4):
    print(i, d)