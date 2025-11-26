# Write a program to count total number of lists in a nested list
my_list = [1,2,3], ["Jafri", "Faisal"], [0.4,4.5],[True, False]

def total_list(my_list):
    total = 0
    for sublist in my_list:
        if type(sublist) == list:
            total += 1
    return total


print(total_list(my_list))