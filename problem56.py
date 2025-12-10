#Write a Python Program to Display element of list with their occurrence

numbers = [ 34,67,89,32,12,45]
result = [(num, numbers.count(num)) for num in numbers]
print(result)