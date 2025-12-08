#write numpy program to repeate array element
import numpy as np
arr = np.array([2,3,4,5])
user_input = int(input("Enter num :"))
r_ar = np.tile(arr,user_input)
print(r_ar)