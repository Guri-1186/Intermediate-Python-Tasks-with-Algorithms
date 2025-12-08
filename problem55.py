# append array element to existing array

from array import *
arr = array('i', [2, 4, 6, 7, 8, 9])  
item = int(input("Enter num :"))
arr.append(item)
print(arr)