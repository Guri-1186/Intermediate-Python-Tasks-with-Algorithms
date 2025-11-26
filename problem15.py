# Write a program to display square of its previous number and next number

number = int(input("Enter a number :"))
def square_of_num(number):
    previus_num = (number - 1) **2
    next_num = (number + 1) **2
    
    return previus_num, next_num

print(square_of_num(number))