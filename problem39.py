#write a numpy program to create two dimensional array, multiplay of any number to taht array elements
import numpy as np
arr = np.array([[1,2,3], [3,4,5], [4,6,7]])
number = int(input("Enter Number: "))

def two_d_arr(number,arr):
    return arr * number
    
     
print(two_d_arr(number,arr))