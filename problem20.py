# write a program to access multiple elements from a list

my_list = [2,4,5,0.6,"cat", "dog", True, False]
def get_multiple_items(my_list):
    start_point = int(input("Enter start point: "))
    end_point = int(input("Enter end point:  "))
    
    return my_list[start_point:end_point +1]


print(get_multiple_items(my_list))