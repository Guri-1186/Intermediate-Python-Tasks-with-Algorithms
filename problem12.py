# write a python program to find most occuring element in a given list of numbers
from statistics import mode
numbers = [2,6,8,9,45,3,4,4,7,0]
def frequency(numbers):
    return mode(numbers)


print(frequency(numbers))
    
    