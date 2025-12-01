#write a numpy program to check element it is nan or not
import numpy as np
def array_isnan(arr):
    return np.isnan(arr)
  

arrat_1d = np.array([30,56,45,34])
print(array_isnan(arrat_1d))
