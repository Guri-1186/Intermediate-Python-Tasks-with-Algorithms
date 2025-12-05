#write a python program to create numpy array, store in a text file and display the result
import numpy as np
arr_1d = np.array([23,45,43,12,10])
np.savetxt("file.txt", arr_1d,fmt="%d")