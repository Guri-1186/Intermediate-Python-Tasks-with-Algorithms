# write a numpy program to create a array of zero. according to user enetred number
import numpy as np

def create_arr(user_input):
    return np.zeros(user_input)


user_input = int(input("Please enter the number :"))
print(create_arr(user_input))