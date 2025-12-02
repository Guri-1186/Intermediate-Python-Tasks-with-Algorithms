#write a python numpy program to make an array of equal shape having same data type of given array
import numpy as np

arr = np.array([1, 2, 3, 4])
print(np.zeros_like(arr))