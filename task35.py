# Declare a plenty_of_arguments function that accepts two parameters (a and b)
# and an additional **kwargs parameter.
#
# The function should return True if the sum of a, b, and the values of 
# **kwargs is greater than 100. It should return False otherwise.
#
# EXAMPLES:
def plenty_of_arguments(a,b,**kwargs):
    result = 0
    for value in kwargs.values():
        result += value
    output = result + a + b
    if output > 100:
        return True
    else:
        return False

    
print(plenty_of_arguments(20, 30)                        ) #  => False
print(plenty_of_arguments(a = 50, b = 75)                ) #  => True
print(plenty_of_arguments(a = 50, b = 25, c = 50)        ) #  => True
print(plenty_of_arguments(a = 25, b = 25, c = 25, d = 25)) #  => False
print(plenty_of_arguments(a = 25, b = 25, c = 25, d = 26)) #  => True