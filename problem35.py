# write a numpy program to add two array
import numpy as np


def add_array(arr_1, arr_2):
    return np.add(arr_1, arr_2)


arr_1 = np.array([34,56,78,90])
arr_2 = np.array([4,56,10,9])

print(add_array(arr_1,arr_2))