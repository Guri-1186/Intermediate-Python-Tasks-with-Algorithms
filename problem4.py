# write a program to get password from the user that contain Alpha numeric and more than 8 and less than 20 character

user_input = input("Enter a word :")
def check_caracter(char):
    if char.isalnum() and 8 < len(char) < 20:
        return f"Password is valid"
    else:
       return f"Wrong password"
   
   
print(check_caracter(user_input))
    