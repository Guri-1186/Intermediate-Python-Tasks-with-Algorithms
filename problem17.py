
# convert lower to upper case and vice versa
user_input = input("Enter a word with Lower and Upper case :")
def swap_char(text):
    if text.lower() == text or text.upper() == text:
         return "Input must contain BOTH lower and upper case letters!"
    return user_input.swapcase()


print(swap_char(user_input))