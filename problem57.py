# Write a Python Pandas program to convert a Numpy array to a Pandas series.
import numpy as np
import pandas as pd
arr = np.array([4,6,7,8,])
ps = pd.Series(arr)
print(ps)