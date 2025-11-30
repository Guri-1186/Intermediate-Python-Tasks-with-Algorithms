# write a program to create dictionary to find addition of all the keys and product of all the 
# values from the dictionary
import math
my_dict = {
    15: 100,
    24: 20,
    36: 33,
    4: 40,
    5: 50
}

def find_additon_product_of_num(my_dict):
    keys = []
    values = []
    for key, value in my_dict.items():
        keys.append(key)
        values.append(value)
    sum_of_keys = sum(keys)
    prod_of_values = math.prod(values)
    return sum_of_keys, prod_of_values

print(find_additon_product_of_num(my_dict))