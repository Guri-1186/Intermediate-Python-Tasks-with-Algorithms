#replace any number in numpy array
import numpy as np
arr = np.array([2,4,6,7,9])
arr[arr%2 == 1] - 1
print(arr)