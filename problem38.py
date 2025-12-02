#write a numpy program to create one dimensional arr, geting number element frome user using for loop
import numpy as np

number = int(input("Enter number of elements: "))
arr = np.zeros(number, np.int64)

for i in range (0,len(arr)):
    element = int(input("Enterelement: "))
    arr[i]=element
print(arr)
    
