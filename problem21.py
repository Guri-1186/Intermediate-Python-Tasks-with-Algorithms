#write e program to get 5 number from the user to sore in list, dipslay all the numbers  with power of 3 using list comperhension

numbers = []
def power_of_three():
    for i in range(5):
        user_input = int(input("Enter 5 number :"))
        numbers.append(user_input)
    
    new_list = [num ** 3 for num in numbers]    
    return new_list
        
print(power_of_three())
    