# create list from existed list that count number less than 20, greater than 5
# solution 1
numbers = [2, 4, 6, 8, 10, 30, 56, 90]
def generate_list(numbers):
    new_list = []
    for num in numbers:
        if num < 20 and num > 5:
            new_list.append(num)
    return new_list

print(generate_list(numbers))  
#solution 2
new_list = [num for num in numbers if 5 < num < 20]

print(generate_list(numbers))