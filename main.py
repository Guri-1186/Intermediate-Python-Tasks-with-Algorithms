
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

# def factorial(num):
#     if num == 1:
#         return 1
#     return num * factorial(num - 1)

# print(factorial(5))
    
# Define a split_in_two function that accepts a list and a number.
# If the number is even, return the list elements from the third element to the end of the list.
# If the number is odd, return the list elements from index 0 (inclusive) to 2 (exclusive)
#
# EXAMPLE:

# def split_in_two(values, num):
#     if num % 2 == 0:
#         return values[2:]
#     else:
#         return values[0:2]
        

# values = ["a", "b", "c", "d", "e", "f"]
# print(split_in_two(values, 3))     
# print(split_in_two(values, 4))    
# print(split_in_two(values, 1))   
# print(split_in_two(values, 10))   


#######################################################################
# Declare a nested_extraction function that accepts a list of lists and an index position.
#
# The function should use the index as the basis of finding both the nested list 
# and the element from that list with the given index position
#
# You can assume the number of lists will always be equal to 
# the number of elements within each of them.
#

# def nested_extraction(n1,ind):
#      result = n1[ind][ind]
#      return result

# n1 = [[3, 4, 5], [7, 8, 9], [10, 11, 12]]
# print(nested_extraction(n1,0))  #=> 3
# print(nested_extraction(n1,1)) # => 8
# print(nested_extraction(n1,2)) # => 12
#################################################################################
# Declare a print(beginning_and_end) function that accepts a list of elements.
#
# It should return True if the first and last elements in the list are equal and False if they are unequal.
#
# Assume the list will always have at least 1 element.
#
# def beginning_and_end(list):
#     if list[0]==list[-1]:
#         return True
#     else:
#         return False
        
    
# print(beginning_and_end([1, 2, 3, 1]))   # => True
# print(beginning_and_end([1, 2, 3, 4, 5])) # => False
# print(beginning_and_end(["a", "b", "a"])) # => True
# print(beginning_and_end([15]))           # => True
############################################################################################
# Declare a long_word_in_collection function that accepts a list and a string. 
# The function should return True if 
#   - the string exists in the list AND
#   - the string has more than 4 characters.
#
# def long_word_in_collection(lst,strs):
#     if strs in words and len(strs) > 4:
#         return True
#     else:
#         return False
    
    
    
# words = ["cat", "dog", "rhino"]
# print(long_word_in_collection(words, "rhino")) # => True
# print(long_word_in_collection(words, "cat"))    #=> False
# # long_word_in_collection(words, "monkey") => False

####################################################################
# Define a sum_of_lengths function that accepts a list of strings.
# The function should return the sum of the string lengths.
#
# EXAMPLES
# sum_of_lengths(["Hello", "Bob"])                  => 8
# sum_of_lengths(["Nonsense"])                      => 8
# sum_of_lengths(["Nonsense", "or", "confidence"])  => 20

# def sum_of_lengths(lst):
#     total = 0
#     for char in lst:
#        total+=len(char)
#     return total
    
    
    
# print(sum_of_lengths(["Hello", "Bob"]))               # => 8
# sum_of_lengths(["Nonsense"])                      => 8
# sum_of_lengths(["Nonsense", "or", "confidence"])

# Define a product function that accepts a list of numbers.
# The function should return the product of the numbers.
# The list will always have at least one value
#
# EXAMPLES

# def product(lst):
#     output = 1
#     for i in lst:
#         output *= i
#     return output

# print(product([1, 2, 3]))   # 6
# print(product([4, 5, 6, 7]))  # 840
# print(product([10]))  # 10

#####################################################################
# Define a smallest_number function  that accepts a list of numbers.
# It should return the smallest value in the list.

# def smallest_number(lst):
#     smallest = lst[0]
#     for num in lst:
#         if num < smallest:
#             smallest = num
#     return smallest



# print(smallest_number([1, 2, 3]))    # => 1
# smallest_number([3, 2, 1])     => 1
# smallest_number([4, 5, 4])     => 4
# smallest_number([-3, -2, -1])  => -3


# Define a concatenate function that accepts a list of strings. 
#
# The function should return a concatenated string which consists of
# all list elements whose length is greater than 2 characters.
#
# def concatenate(lst):
#      word = ""
#      for char in lst:
#          word+=char
#      return word

# print(concatenate(["abc", "def", "ghi"]))      #=> "abcdefghi"
# concatenate(["abc", "de", "fgh", "ic"]) => "abcfgh"
# concatenate(["ab", "cd", "ef", "gh"])   => ""
####################################################################################
# Define a super_sum function that accepts a list of strings. 
# The function should sum the index positions of the first occurence of the letter “s” in each word. 
#
# Not every word is guaranteed to have an “s”.
# Don’t use "sum" as a variable name as it’s a built-in keyword.
#

# def super_sum(lst):
#     total = 0
#     for word in lst:
#         index = word.lower().find("s")
#         total+=index
#     return total
        
            
# print(super_sum([]))                              # => 0
# print(super_sum(["mustache"]))                    # => 2
# super_sum(["mustache", "greatest"])           => 8
# super_sum(["mustache", "pessimist"])          => 4
# super_sum(["mustache", "greatest", "almost"]) => 12

