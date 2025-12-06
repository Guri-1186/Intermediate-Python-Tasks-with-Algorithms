# Write factors function that accepts a positive whole number
# It should return a list of all of the number'print(factors in ) #ascending order
# HINT: Could the range function be helpful here? Or maybe a while loop?
#
# EXAMPLES

def factors(num):
    my_factors = []
    for i in range (1, num + 1):
        if num % i == 0:
            my_factors.append(i)
    return my_factors
    
 
print(factors(1) ) # => [1]
print(factors(2) ) # => [1, 2]
print(factors(10)) # => [1, 2, 5, 10]
print(factors(64)) # => [1, 2, 4, 8, 16, 32, 64]