# write a program to reverse substring from string
user_input = input("Enter a string :")
def reverse_substring(user_input):
    
    starting = int(input("enter a starting number :"))
    ending = int(input("enter a starting number :"))
    new_string = user_input[starting:ending]
    return new_string[::-1]


print(reverse_substring(user_input))