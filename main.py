
# def count_down_from(number):
#     start = number
#     while start > 0:
#         start -= 1
        
# def count_down_from(number):
#     if number <= 0:
#         return
#     print(number)
#     count_down_from(number -1)
  
# count_down_from(5)


# def reverse(str):
#     start_index = 0
#     last_index = len(str) -1
#     reverse_string = ""
#     while last_index >= start_index:
#         reverse_string += str[last_index]
#         last_index -= 1
#     return reverse_string
    
# print(reverse("straw")) 

# def reverse(str):
#   if len(str) <= 1:
#       return str
#   return str[-1] + reverse(str[:-1])

    
# print(reverse("straw")) 

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)

print(factorial(5))
    