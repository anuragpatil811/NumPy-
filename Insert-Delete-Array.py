#Insert and delete arrays functions 
import numpy as np
var = np.array([1, 2, 3, 4])
#print(var)
#v=np.insert(var, 2, 40)
x = np.append(var, 6.5)
v=np.insert(var, (2, 4), 6.5)
#print(v)
#print(x)

var1 = np.array([[1, 2, 3], [1, 2, 3]])
#v1 = np.insert(var1,2, 6, axis=1)
v1 = np.append(var1, [[45, 44, 23]], axis=0)
#print(v1)

#DELETE
var = np.array([1, 2, 3, 4])
print(var)
d = np.delete(var, 2)
print(d)
