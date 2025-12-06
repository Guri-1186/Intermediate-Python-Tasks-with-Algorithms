# Declare a sum_from function that accepts two numbers as arguments.
# The second number will always be greater than the first number.
# The function should return the sum of all numbers from the first number to the second number (inclusive).

# EXAMPLES

def sum_from(num1,num2):
    result = 0
    for num in range (num1, num2+1):
        result+=num
    return result
        
    
print(sum_from(1, 2))   # 1 + 2                  => 3
print(sum_from(1, 5))   # 1 + 2 + 3 + 4 + 5      => 15
print(sum_from(3, 8))   # 3 + 4 + 5 + 6 + 7 + 8  => 33
print(sum_from(9, 12))  # 9 + 10 + 11 + 12       => 42