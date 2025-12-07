# create set that display only even number
numbers = set()
def even_nums(numbers):
    for i in range(5):
        user_input = int(input("Enter a number :"))
        numbers.add(user_input)
    even_set = {num for num in numbers if num % 2 == 0}
    return even_set
      
     
print(even_nums(numbers))
    
    
