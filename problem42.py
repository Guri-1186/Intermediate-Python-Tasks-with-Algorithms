# write a python program to convert array element to boolean value
import numpy as np
arr_1d = np.array([1,1,0,0,1,1])
bool_arr = arr_1d.astype('bool')
print(bool_arr)