# write a program to get length in mm and convert to m and km 
user_input = int(input("Enter length in mm :"))
def measurment_converter(mm):
    m = mm/1000
    km = mm/1_000_000
    
    return m, km

print(measurment_converter(user_input))