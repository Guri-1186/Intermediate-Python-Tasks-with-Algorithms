#Write a Python Program to display only those number that are divisible by 4 or 5 from list, using list comprehension.   

numbers = [20,16,7,3]
result = [num for num in numbers if num % 4 == 0 or num % 5 == 0]
print(result)
