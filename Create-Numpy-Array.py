import numpy as np
#Creating Numpy Array
"""""
#x = [1, 2, 3, 4]
#y = np.array(x)
y = np.array([1, 2, 3, 4])
print(y)
print(type(y))
print(y.ndim)
"""

#From empty list to array
"""""
l = []
for i in range(1, 5):
    int_1 = int(input("Enter:"))
    l.append(int_1)
print(np.array(l))
"""

#2-D array
"""""
ar2 = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
print(ar2)
print(ar2.ndim)
"""""
#3-D array
"""""
ar3 = np.array([[[1, 2, 3, 4], [1, 2, 3, 4], [1,2,3, 4]]])
print(ar3)
print(ar3.ndim)
"""
#High dimensional array
arn = np.array([1,2,3,4], ndmin=10)
print(arn)
print(arn.ndim)