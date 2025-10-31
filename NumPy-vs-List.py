#program to differentiate between NumPy array and List in Python
#import timeit
#print(timeit.timeit('[j**4 for j in range(1, 9)]'))
import numpy as np
import timeit

stmt = "np.arange(1, 9)**4"
setup = "import numpy as np"
print(timeit.timeit(stmt=stmt, setup=setup, number=10000))

#in Jupyter Notebook:
#%timeit[j**4 for j in range(1, 9)]
#import numpy as np
#import timeit
#%timeit np.arange(1, 9)**4