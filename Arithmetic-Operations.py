import numpy as np
#**Addition**
var = np.array([1, 2, 3, 4])
#varadd = var + 3
#print(varadd)

var1 = np.array([1, 2, 3, 4])
var2 = np.array([1, 2, 3, 4])
varadd = np.add(var1, var2)
#varadd = var1 + var2
#print(varadd)

#**Subtraction**
var = np.array([1, 2, 3, 4])
varadd = var - 3
#print(varadd)

#**Multiplication**
var = np.array([1, 2, 3, 4])
varadd = var * 3
#print(varadd)

#**Division**
var = np.array([1, 2, 3, 4])
varadd = var / 3
#print(varadd)

#**Modulus**
var = np.array([1, 2, 3, 4])
varadd = var % 3
#print(varadd)

#**Reciprocal**
var = np.array([1, 2, 3, 4])
varadd = np.reciprocal(var)
print(varadd)

#***2D ARRAY***
var21 = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
var22 = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
#print(var21)
#print()
#print(var22)
#print()
varadd = var21 + var22
#print(varadd)